from django.contrib.admin.utils import quote, unquote
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views import View

from wagtail.admin.modal_workflow import render_modal_workflow


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

    def get_object_id(self, instance):
        return instance.pk

    def get_object_string(self, instance):
        return str(instance)

    def get_chosen_url(self, instance):
        object_id = self.get_object_id(instance)
        return reverse(self.chosen_url_name, args=(quote(object_id),))

    def paginate(self):
        self.paginator = Paginator(self.object_list, per_page=self.paginate_by)
        self.object_list = self.paginator.get_page(self.request.GET.get('p'))

    def get_rows(self):
        for item in self.object_list:
            yield self.get_row_data(item)

    def get_row_data(self, item):
        return {
            'choose_url': self.get_chosen_url(item),
            'title': self.get_object_string(item),
        }

    def get_context_data(self):
        return {
            'icon': self.icon,
            'page_title': self.page_title,
            'rows': self.get_rows(),
        }

    def get_template(self):
        return self.template

    def get_object_list(self):
        return self.model.objects.all()


class ChosenView(View):

    # URL route name for editing an existing item - should return the URL of the item's edit view
    # when reversed with the item's quoted ID as its only argument. If no suitable URL route exists
    # (e.g. it requires additional arguments), subclasses can override get_edit_item_url instead.
    edit_item_url_name = None

    model = None

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get_object_id(self, instance):
        return instance.pk

    def get_edit_item_url(self, instance):
        if self.edit_item_url_name is None:
            return None
        else:
            object_id = self.get_object_id(instance)
            return reverse(self.edit_item_url_name, args=(quote(object_id),))

    def get_object_string(self, instance):
        return str(instance)

    def get_response_data(self, item):
        return {
            'id': str(self.get_object_id(item)),
            'string': self.get_object_string(item),
            'edit_link': self.get_edit_item_url(item)
        }

    def get(self, request, pk):
        try:
            item = self.get_object(unquote(pk))
        except (ObjectDoesNotExist if self.model is None else self.model.DoesNotExist):
            raise Http404

        response_data = self.get_response_data(item)

        return render_modal_workflow(
            request,
            None, None,
            None, json_data={'step': 'chosen', 'result': response_data}
        )
