from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from generic_chooser.views import ModelChooserMixin, ModelChooserViewSet

from bakerydemo.base.models import Person


class PersonChooserMixin(ModelChooserMixin):
    preserve_url_parameters = [
        "job_title",
    ]  # preserve this URL parameter on pagination / search

    def get_edit_item_url(self, item):
        return reverse("wagtailsnippets_base_person:edit", args=(quote(item.pk),))

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        job_title = self.request.GET.get("job_title")
        if job_title:
            objects = objects.filter(job_title=job_title)
        return objects


class PersonChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = Person
    page_title = _("Choose a person")
    per_page = 10
    order_by = "first_name"
    fields = ["first_name", "last_name", "job_title"]
    chooser_mixin_class = PersonChooserMixin
