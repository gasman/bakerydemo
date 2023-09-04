from .views import pokemon_chooser_viewset

PokemonChooserBlock = pokemon_chooser_viewset.get_block_class(
    name="PokemonChooserBlock", module_path="bakerydemo.pokemon.blocks"
)
