from django.urls import path
from wagtail import hooks

from .views import PokemonIndexView, pokemon_chooser_viewset


@hooks.register("register_admin_urls")
def register_pokemon_index():
    return [
        path(
            "pokemon/",
            PokemonIndexView.as_view(),
            name="pokemon_index",
        )
    ]


@hooks.register("register_admin_viewset")
def register_pokemon_chooser_viewset():
    return pokemon_chooser_viewset