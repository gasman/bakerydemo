GENERIC_CHOOSER_MODAL_ONLOAD_HANDLERS = {
    'choose': function(modal, jsonData) {
        $('a.item-choice', modal.body).on('click', function() {
            modal.loadUrl(this.href);
            return false;
        });
    },
    'chosen': function(modal, jsonData) {
        modal.respond('chosen', jsonData['result']);
        modal.close();
    }
};
