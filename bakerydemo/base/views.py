from wagtail.admin.ui.tables import Column
from wagtail.admin.views.generic import IndexView
from wagtail.admin.viewsets.chooser import ChooserViewSet


class PersonChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "base.Person"

    icon = "user"
    choose_one_text = "Choose a person"
    choose_another_text = "Choose another person"
    edit_item_text = "Edit this person"
    form_fields = ["first_name", "last_name"]  # fields to show in the "Create" tab
    preserve_url_parameters = ["multiple", "first_name"]
    url_filter_parameters = ["first_name"]


person_chooser_viewset = PersonChooserViewSet("person_chooser")

PersonChooserWidget = person_chooser_viewset.widget_class
