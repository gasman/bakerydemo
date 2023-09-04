from wagtail.admin.ui.tables import Column
from wagtail.admin.views.generic import IndexView
from wagtail.admin.viewsets.chooser import ChooserViewSet

from .models import Pokemon


class PokemonIndexView(IndexView):
    model = Pokemon
    paginate_by = 20
    columns = [
        Column("id"),
        Column("name"),
    ]


class PokemonChooserViewSet(ChooserViewSet):
    model = Pokemon

    icon = "snippet"
    choose_one_text = "Choose a pokemon"
    choose_another_text = "Choose another pokemon"
    edit_item_text = "Edit this pokemon"


pokemon_chooser_viewset = PokemonChooserViewSet("pokemon_chooser")
