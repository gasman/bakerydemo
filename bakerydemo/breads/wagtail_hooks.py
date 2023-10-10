from django.utils.safestring import mark_safe
from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from bakerydemo.breads.models import BreadIngredient, BreadType, Country, Region


class BreadIngredientSnippetViewSet(SnippetViewSet):
    model = BreadIngredient
    ordering = ("name",)
    search_fields = ("name",)
    inspect_view_enabled = True


class BreadTypeSnippetViewSet(SnippetViewSet):
    model = BreadType
    ordering = ("title",)
    search_fields = ("title",)


class CountrySnippetViewSet(SnippetViewSet):
    model = Country
    ordering = ("title",)
    search_fields = ("title",)


class RegionSnippetViewSet(SnippetViewSet):
    model = Region
    ordering = ("name",)
    search_fields = ("name",)


# We want to group several snippets together in the admin menu.
# This is done by defining a SnippetViewSetGroup class that contains a list of
# SnippetViewSet classes.
# When using a SnippetViewSetGroup class to group several SnippetViewSet classes together,
# you only need to register the SnippetViewSetGroup class with Wagtail.
# No need to register the individual SnippetViewSet classes.
#
# See the documentation for SnippetViewSet for more details.
# https://docs.wagtail.org/en/stable/reference/viewsets.html#snippetviewsetgroup
class BreadMenuGroup(SnippetViewSetGroup):
    menu_label = "Bread Categories"
    menu_icon = "suitcase"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        BreadIngredientSnippetViewSet,
        BreadTypeSnippetViewSet,
        CountrySnippetViewSet,
        RegionSnippetViewSet,
    )


register_snippet(BreadMenuGroup)


@hooks.register('insert_editor_js')
def editor_js():
    return mark_safe(
        """
        <script>
            window.addEventListener('DOMContentLoaded', (event) => {
                const regionCheckboxes = document.querySelectorAll('input[name="regions"]');
                const countryCheckboxes = document.querySelectorAll('input[name="countries_of_origin"]');
                const setCountryVisibility = () => {
                    const regionIsEnabled = {};
                    for (const checkbox of regionCheckboxes) {
                        regionIsEnabled[checkbox.value] = checkbox.checked;
                    }
                    for (const checkbox of countryCheckboxes) {
                        const region = checkbox.dataset.region;
                        if (regionIsEnabled[region]) {
                            checkbox.parentNode.parentNode.style.display = 'block';
                        } else {
                            checkbox.parentNode.parentNode.style.display = 'none';
                        }
                    }
                };
                if (regionCheckboxes.length && countryCheckboxes.length) {
                    setCountryVisibility();
                    for (const checkbox of regionCheckboxes) {
                        checkbox.addEventListener('change', setCountryVisibility);
                    }
                }
            });
        </script>
        """
    )
