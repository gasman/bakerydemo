from django.contrib.admin.utils import unquote
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views import View

from wagtail.admin.modal_workflow import render_modal_workflow
from wagtail.utils.pagination import paginate


class ChooseView(View):
    icon = 'snippet'
    page_title = _("Choose")
    template = 'generic_chooser/choose.html'
    paginate_by = None

    def get(self, request):
        self.object_list = self.get_object_list()

        # Pagination
        if self.paginate_by:
            self.paginate()

        return render_modal_workflow(
            request,
            self.get_template(), None,
            self.get_context_data(), json_data={'step': 'choose'}
        )

    def paginate(self):
        self.paginator, self.object_list = paginate(self.request, self.object_list, per_page=self.paginate_by)

    def get_context_data(self):
        return {
            'icon': self.icon,
            'page_title': self.page_title,
            'items': self.object_list,
            'chosen_url_name': self.chosen_url_name,
        }

    def get_template(self):
        return self.template

    def get_object_list(self):
        return self.model.objects.all()


class ChosenView(View):
    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get_response_data(self, item):
        return {
            'id': str(item.pk),
            'string': str(item),
            'edit_link': self.get_edit_url(item)
        }

    def get(self, request, pk):
        try:
            item = self.get_object(pk=unquote(pk))
        except self.model.DoesNotExist:
            raise Http404

        response_data = self.get_response_data(item)

        return render_modal_workflow(
            request,
            None, None,
            None, json_data={'step': 'chosen', 'result': response_data}
        )
