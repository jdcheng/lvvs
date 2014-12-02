from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^toballot/$', views.toballot, name='toballot'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>\d+)/previous_vote/$', views.vote_previous, name='vote_previous'),
    url(r'^(?P<question_id>\d+)/forward/$', views.forward, name='forward'),
    url(r'^(?P<question_id>\d+)/back/$', views.back, name='back'),
    url(r'^review/$', views.ReviewView.as_view(), name='review'),
    url(r'^survey/$', views.get_new_survey, name='survey'),
    url(r'^slider/$', views.slider, name='slider'),
    url(r'^options/$', views.options_base, name='options'),
    url(r'^options/$', views.options_review, name='options_review'),
    url(r'^options/submit/$', views.submit_options, name='submit_options'),
    url(r'^(?P<question_id>\d+)/options/$', views.options, name='options'),
    url(r'^newsurvey/$', views.get_new_survey, name='new_survey'),
    url(r'^help/$', views.help, name='help'),
    url(r'^$', views.options_initial, name='options_initial'),
    url(r'^survey/options/$', views.options_survey, name='options_survey'),
    url(r'^$', views.welcome, name='welcome'),
)