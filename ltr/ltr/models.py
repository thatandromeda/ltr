from django.core.urlresolvers import reverse
from django.db import models
from taggit.managers import TaggableManager

class Questionnaire(models.Model):
    name = models.CharField(max_length=50)    
    q1 = models.TextField(help_text="Tell me a bit about you -- your job, your institution.", blank=True, null=True)
    q2 = models.TextField(help_text="How much of your job is about coding?  Do you have any formal code responsibilities, or is this simply a skill that you bring to your formal responsibilities?")
    q3 = models.TextField(help_text="Have you had support from your employer in learning to code/spending that much time coding?")
    q4 = models.TextField(help_text="What would you recommend to someone implementing code like this/what did you learn?")
    q5 = models.TextField(help_text="What would you recommend to someone who wanted to learn to write code like this?")
    q6 = models.TextField(null=True, blank=True, help_text="If you're a manager, how have you supported employees in learning to code?")
    tags = TaggableManager(blank=True)
    
    @property
    def first_owner(self):
        try:
            persons = self.person.all()
            return persons[0].name
        except IndexError, AttributeError:
            return None

    def get_absolute_url(self):
        return reverse('questionnaire_detail_view', args=(self.pk,))

    def __unicode__(self):
        if self.first_owner:
            return self.first_owner + "'s questionnaire"
        else:
            return self.name

    class Meta:
        ordering = ['name']

class Person(models.Model):

    TYPE_CHOICES = (
      ('UNI', 'Academic'),
      ('K12', 'School'),
      ('PUB', 'Public'),
      ('SPE', 'Special'),
      ('VND', 'Vendor'),
      ('ARC', 'Archives'),
      ('OTH', 'Other'),
    )
  
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=50)
    library_type = models.CharField(max_length=3,
                                      choices=TYPE_CHOICES)
    library_role = TaggableManager()
    questionnaire = models.ForeignKey(Questionnaire, db_index = True, related_name="person", null=True, blank=True)

    @property
    def scripts(self):
        return Script.objects.filter(questionnaire=self.questionnaire)

    def get_absolute_url(self):
        return reverse('person_detail_view', args=(self.pk,))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Script(models.Model):
    name = models.CharField(max_length=50)
    language = TaggableManager()
    problem_solved = models.TextField(help_text="What problem did this code solve?")
    impact = models.TextField(help_text="What was the impact of this code?")
    source = models.CharField(max_length=100)
    permission = models.BooleanField(default=False)
    permission_notes = models.CharField(max_length=50, null=True, blank=True)
    questionnaire = models.ForeignKey(Questionnaire, db_index = True, related_name="script", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('script_detail_view', args=(self.pk,))

    def __unicode__(self):
        try:
            return self.questionnnaire.all()[0].first_owner + "'s script"
        except AttributeError:
            return self.name
