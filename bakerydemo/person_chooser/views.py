from django.contrib.admin.utils import quote, unquote
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views import View

from wagtail.admin.modal_workflow import render_modal_workflow

from bakerydemo.base.models import People


class GenericChooseView(View):
    icon = 'snippet'
    page_title = _("Choose")
    template = 'person_chooser/choose_generic.html'

    def get(self, request):
        return render_modal_workflow(
            request,
            self.get_template(), None,
            self.get_context_data(), json_data={'step': 'choose'}
        )

    def get_context_data(self):
        return {
            'icon': self.icon,
            'page_title': self.page_title,
            'items': self.get_object_list(),
            'chosen_url_name': self.chosen_url_name,
        }

    def get_template(self):
        return self.template

    def get_object_list(self):
        return self.model.objects.all()


class ChoosePersonView(GenericChooseView):
    icon = 'user'
    model = People
    page_title = _("Choose a person")
    chosen_url_name = 'person_chooser:chosen_person'


class ChosenPersonView(View):
    def get(self, request, pk):
        item = get_object_or_404(People, pk=unquote(pk))

        person_data = {
            'id': str(item.pk),
            'string': str(item),
            'edit_link': reverse('wagtailsnippets:edit', args=(
                'base', 'people', quote(item.pk)))
        }

        return render_modal_workflow(
            request,
            None, None,
            None, json_data={'step': 'chosen', 'result': person_data}
        )
