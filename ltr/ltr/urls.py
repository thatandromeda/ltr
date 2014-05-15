from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

admin.autodiscover()


person_pages = patterns('',
    url(r'^$',
        views.PersonListView.as_view(),
        name='person_list_view'),
    url(r'^create/$',
        views.PersonCreateView.as_view(),
        name='person_create_view'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.PersonDetailView.as_view(),
        name='person_detail_view'),
    url(r'^type/(?P<type>[0-9A-Z]+)/$',
        views.PersonByTypeListView.as_view(),
        name='person_by_type_list_view'),
)

script_pages = patterns('',
    url(r'^$',
        views.ScriptListView.as_view(),
        name='script_list_view'),
    url(r'^create/$', 
        views.ScriptCreateView.as_view(),
        name='script_create_view'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.ScriptDetailView.as_view(),
        name='script_detail_view'),
)

questionnaire_pages = patterns('',
    url(r'^$', 
        views.QuestionnaireListView.as_view(),
        name='questionnaire_list_view'),
    url(r'^create/$', 
        views.QuestionnaireCreateView.as_view(),
        name='questionnaire_create_view'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.QuestionnaireDetailView.as_view(),
        name='questionnaire_detail_view'),
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ltr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^persons/', include(person_pages)),
    url(r'^scripts/', include(script_pages)),
    url(r'^questionnaires/', include(questionnaire_pages)),
)
