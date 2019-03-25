GENERIC_CHOOSER_MODAL_ONLOAD_HANDLERS = {
    'choose': function(modal, jsonData) {
        function ajaxifyLinks(context) {
            $('a.item-choice', context).on('click', function() {
                modal.loadUrl(this.href);
                return false;
            });
        }
        ajaxifyLinks(modal.body);

        var searchUrl = $('form.chooser-search', modal.body).attr('action');
        var searchRequest;

        function search() {
            searchRequest = $.ajax({
                url: searchUrl,
                data: {q: $('#id_q').val(), results: 'true'},
                success: function(data, status) {
                    searchRequest = null;
                    $('#search-results').html(data);
                    ajaxifyLinks($('#search-results'));
                },
                error: function() {
                    searchRequest = null;
                }
            });
            return false;
        }

        $('form.snippet-search', modal.body).on('submit', search);

        $('#id_q').on('input', function() {
            if(searchRequest) {
                request.abort();
            }
            clearTimeout($.data(this, 'timer'));
            var wait = setTimeout(search, 50);
            $(this).data('timer', wait);
        });

    },
    'chosen': function(modal, jsonData) {
        modal.respond('chosen', jsonData['result']);
        modal.close();
    }
};
