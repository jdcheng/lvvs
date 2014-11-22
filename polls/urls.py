from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^survey/$', views.toballot, name='toballot'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>\d+)/forward/$', views.forward, name='forward'),
    url(r'^(?P<question_id>\d+)/back/$', views.back, name='back'),
    url(r'^survey/$', views.survey, name='survey'),
    url(r'^survey/submit/$', views.submit_survey, name='submit_survey'),
    url(r'^options/$', views.options_base, name='options'),
    url(r'^options/submit/$', views.submit_options, name='submit_options'),
    url(r'^(?P<question_id>\d+)/options/$', views.options, name='options'),
    url(r'^sizeform/$', views.get_title_size, name='get_title_size'),
    url(r'^newsurvey/$', views.get_new_survey, name='new_survey'),

)