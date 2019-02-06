from django.conf.urls import url

from bakerydemo.person_chooser.views import ChoosePersonView, ChosenPersonView

app_name = 'person_chooser'
urlpatterns = [
    url(r'^chooser/$', ChoosePersonView.as_view(), name='choose_person'),
    url(r'^chooser/(\d+)/$', ChosenPersonView.as_view(), name='chosen_person'),
]
