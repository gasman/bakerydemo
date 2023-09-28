from wagtail import hooks
from django.utils.safestring import mark_safe

@hooks.register('insert_editor_js')
def editor_js():
    return mark_safe(
        """
        <script>
            window.addEventListener('DOMContentLoaded', (event) => {
                const versionSelector = document.querySelector('#id_version');

                const setStateForVersion = () => {
                    const version = versionSelector.value;
                    const preface = document.querySelector('#panel-child-content-preface-section');

                    if (version === 'heavy') {
                        preface.style.display = 'block';
                    } else {
                        preface.style.display = 'none';
                    }
                };
                if (versionSelector) {
                    setStateForVersion();
                    versionSelector.addEventListener('change', setStateForVersion);
                }
            });
        </script>
        """
    )
