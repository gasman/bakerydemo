from django.conf.urls import url

from bakerydemo.person_chooser import views

app_name = 'person_chooser'
urlpatterns = [
    url(r'^chooser/$', views.ChoosePersonView.as_view(), name='choose_person'),
    url(r'^chooser/(\d+)/$', views.ChosenPersonView.as_view(), name='chosen_person'),
    url(r'^page-chooser/$', views.ChoosePageAPIView.as_view(), name='choose_page'),
    url(r'^page-chooser/(\d+)/$', views.ChosenPageAPIView.as_view(), name='chosen_page'),
]
