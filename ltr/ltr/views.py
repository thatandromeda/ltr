from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from taggit.models import TaggedItem
from .models import Person, Questionnaire, Script

#
# Generic views
#

class LTRCreateView(CreateView):
    template_name = "ltr/create_form.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(LTRCreateView, self).get_context_data(*args, **kwargs)
        context['entity'] = self.get_form_class()._meta.model
        
        # This is a stupid hack to get the complete list of tags for each
        # model. There doesn't seem to be an easy way to do this.
        # The 'extra' bit is so that the sort will be case-insensitive:
        # http://stackoverflow.com/questions/3409047/django-orm-case-insensitive-order-by
        generic_tagged_item = TaggedItem.objects.all()[0]
        context['person_tags'] = generic_tagged_item.tags_for(Person).extra(\
            select={'lower_name':'lower(name)'}).order_by('lower_name')
        context['script_tags'] = generic_tagged_item.tags_for(Script).extra(\
            select={'lower_name':'lower(name)'}).order_by('lower_name')
        context['questionnaire_tags'] = generic_tagged_item.tags_for(Questionnaire).extra(\
            select={'lower_name':'lower(name)'}).order_by('lower_name')
        return context


#
# Person views
#

class PersonListView(ListView):
    model = Person
    
class PersonCreateView(LTRCreateView):
    model = Person
    success_url = reverse_lazy('person_list_view')

class PersonDetailView(DetailView):
    model = Person

class PersonByTypeListView(ListView):
    def get_queryset(self, **kwargs):
        persons = Person.objects.filter(library_type=self.kwargs['type'])
        return persons

#
# Script views
#

class ScriptListView(ListView):
    model = Script

class ScriptCreateView(LTRCreateView):
    model = Script
    success_url = reverse_lazy('script_list_view')

class ScriptDetailView(DetailView):
    model = Script

    
#
# Questionnaire views
#

class QuestionnaireListView(ListView):
    model = Questionnaire

class QuestionnaireCreateView(LTRCreateView):
    model = Questionnaire
    success_url = reverse_lazy('questionnaire_list_view')

class QuestionnaireDetailView(DetailView):
    model = Questionnaire
