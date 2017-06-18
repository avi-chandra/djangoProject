from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name = "index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = "detail"),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name = "results"),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name = "vote"),
    url(r'^viewdata/$', views.viewData, name = "viewdata"),
    url(r'^register/$', views.register, name = "register"),
    url(r'^thanks/$', views.thanks, name = "thanks"),
    url(r'^signup/$',views.SignUpView.as_view(), name = "signup"),
    url(r'^ajax/ValidateUser/$',views.ValidateUser, name = "ValidateUser"),
    url(r'^ajax/ValidateId/$',views.ValidateId, name = "ValidateId"),
    url(r'^api/play_count_by_month', views.play_count_by_month, name='play_count_by_month'),
]