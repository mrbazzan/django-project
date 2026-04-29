'use strict';
{
    const $ = django.jQuery;

    function init($elements) {
        $elements.not('.select2-hidden-accessible').each(function () {
            let options = {};
            if (this.dataset.select2Options) {
                try {
                    options = JSON.parse(this.dataset.select2Options);
                } catch (e) {
                    options = {};
                }
            }
            $(this).select2(options);
        });
    }

    $(function () {
        init($('select.admin-select2-tag'));
    });

    $(document).on('formset:added', function (event) {
        init($(event.target).find('select.admin-select2-tag'));
    });
}
