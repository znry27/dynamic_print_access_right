odoo.define('dynamic_print_access_right.print_domain_widget', function (require) {
"use strict";

    var BasicFields = require('web.basic_fields');
    var core = require('web.core');
    var registry = require('web.field_registry');

    var qweb = core.qweb;
    var _t = core._t;
    var _lt = core._lt;


    var PrintDomain = BasicFields.FieldDomain.extend({
        _render: function () {
            if(this.recordData['condition_model'] && this.recordData['condition_model'] != this._domainModel){
                this._domainModel = this.recordData['condition_model'];
                this.domainSelector = false;
            }

            return this._super.apply(this, arguments);
        },
        _replaceContent: function () {
            if (this._$content) {
                this._$content.remove();
            }
            this._$content = $(qweb.render("PrintDomain.content", {
                hasModel: !!this._domainModel,
                isValid: !!this._isValidForModel,
                nbRecords: this.nbRecords,
                inDialogEdit: this.inDialog && this.mode === "edit",
            }));
            this._$content.appendTo(this.$el);
        },
    });

    registry.add('print_domain', PrintDomain);

});
