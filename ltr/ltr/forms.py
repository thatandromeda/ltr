from django import forms

from .models import Person, Questionnaire

class BetterQuestionnaireForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    help_text="Generate a foreign key here!",
                                    required=False)

    class Meta:
        model = Questionnaire