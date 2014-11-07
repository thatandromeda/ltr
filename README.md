This is the Django app I wrote to keep track of my survey data for my [ALA TechSource](http://www.alatechsource.org/) Library Technology Report (due out early 2015) on how librarians use short programs to improve their work.

# Installation

This assumes that you have installed [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/), which you should do anyway if you haven't because it's amazing. `virtualenvwrapper` in turn expects [pip](http://pip.readthedocs.org/), which is even more amazing.  Once you've got those...

* download the ZIP file of this repository and unzip it into the directory of your choice (or git clone it, if you speak git)
* `cd` into your project directory
* `mkvirtualenv ltr`
* `workon ltr`
* `pip install -r requirements.txt`
* `python ltr/manage.py runserver`
* point your browser at `127.0.0.1:8000`
* (when you're done playing around for now) `deactivate`
* (next time you want to play around, you'll need to `workon ltr` again, but you won't need to install the requirements unless they have been updated)

I haven't made a home page template, so you'll get an error message at that page, but it will list the URLs it does know about. There's no content yet (the `.gitignore` keeps my sqlite3 database out of the repository, because you shouldn't have my raw research data), so go ahead and add your own to see what it looks like! (Don't worry; your .sqlite3 files will be kept out of the repo, too.)

# Learning more
The [Django tutorial](https://docs.djangoproject.com/en/1.7/intro/tutorial01/) is a starting point for many Djangonauts, and the rest of the [Django documentation](https://docs.djangoproject.com/) references it heavily.

I got started with [The Django Book](http://www.djangobook.com/en/2.0/index.html), which by now is hugely out of date but was an excellent tutorial. (Helping bring it up-to-date might be a fine way for you to learn Django, as well as a public service!)

[Two Scoops of Django](http://twoscoopspress.org/) is __the__ guide to Django best practices.

I didn't know about the amazing [django-cookie-cutter](https://github.com/pydanny/cookiecutter-django) when I started this project, but if I had I would have used it; it's a great timesaver.

I got my start with python through the [Google Python course](https://developers.google.com/edu/python/), which is outstanding if you already have some background in general programming concepts.

# Improving this code

You are welcome to use this repository as a basis for learning Django and improving your own coding skills!  Some things you might try...

* writing an actual home page (this mostly depends on HTML skills, plus adding one line to the `urls.py` file by analogy with existing lines)
* adding delete and edit pages (use Django's built-in `DeleteView` and `UpdateView`)
* adding a page which lists all the tags in the system, with links to the tag detail pages
* improving the workflow for adding new people with their surveys and questionnaires (I have made it only as good as it needed to be to not outright irritate me; the usability's still not great)
