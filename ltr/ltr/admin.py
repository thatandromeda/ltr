from django.contrib import admin

from models import Person, Script, Questionnaire

class PersonAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'library_type', 'questionnaire')
    list_filter = ('library_type',)
admin.site.register(Person, PersonAdmin)

class ScriptAdmin(admin.ModelAdmin):
    search_fields = ('language',)
    list_display = ('name', 'questionnaire')
    list_filter = ('permission',)
admin.site.register(Script, ScriptAdmin)

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('first_owner', 'script')
admin.site.register(Questionnaire, QuestionnaireAdmin)
