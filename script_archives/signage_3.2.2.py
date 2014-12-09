import glob
import os
import pandas as pd
import sys
import shutil
import datetime

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
dest_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2])
print current_dir

directory = os.path.sep.join(current_dir.split(os.path.sep)[:-3])


oldcsvfiles = csvfiles = os.path.join(dest_dir, '*.csv')
for oldcsvfile in glob.glob(oldcsvfiles):
    filename = os.path.basename(oldcsvfile)
    print 'Removing ' + filename
    os.remove(oldcsvfile)

csvfiles = os.path.join(directory, '*.csv')
for csvfile in glob.glob(csvfiles):
   
    filename = os.path.splitext(csvfile)[0]#<--to get filename w/o extension
    print filename
    if '_live' in filename:
        print "Remove this file"
        os.remove(csvfile)

csvfiles = os.path.join(directory, '*.csv')
for csvfile in glob.glob(csvfiles):

    filename = csvfile

    df = pd.read_csv(filename)
    df = df.fillna('')
    df = df.astype(str)

   
    df.ix[df['CONTACT PHONE NUMBER'].str.contains("nosign"), ['CONTACT PHONE NUMBER', 'CONTACT NAME']] = "N/A"
   
    df = df[~df["ORGANIZATION"].str.contains("WPPL",case=False)]
    df = df.sort('MEETING START TIME')
    date = df["DATE"].irow(0)
    print"Printing date: " + date;
    month,day,year = (int(x) for x in date.split('/'))
    """print month
    print day
    print year"""
    day=datetime.date(year,month,day)
  
    weekday = day.strftime("%A")

    df['CONTACT PHONE NUMBER']=df['CONTACT PHONE NUMBER'].apply(lambda x: (x and '('+x[:3]+')'+x[3:6]+'-'+x[6:10]) or '')
    df['DATE']=df['DATE'].apply(lambda x: weekday[:3] + '. ' + x)
    print 'Weekday strip ' + weekday[:3]
    df.to_csv(weekday + '_live.csv', cols=["DATE","MEETING START TIME","MEETING END TIME","DESCRIPTION","ORGANIZATION","CONTACT NAME","CONTACT PHONE NUMBER","LOCATION"],index=False)

movefiles = os.path.join(current_dir, '*_live.csv')#current_dir: very important!
print "destination directory" + dest_dir
for movefile in glob.glob(movefiles):
    print "Movefile " + movefile
    movefilename = movefile
    shutil.move(movefilename, dest_dir)
raw_input("Press enter to close")
