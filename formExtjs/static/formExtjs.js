Ext.onReady(function() {
    Ext.apply(Ext.form.VTypes, {
    	commaSeparatedIntegerText: Ext.form.field.Base.prototype.invalidText,
        commaSeparatedIntegerMask: /[\d\,]/,
        commaSeparatedIntegerRe: /^\d+(,\d+)*$/,
        commaSeparatedInteger: function(value){
        return Ext.form.VTypes.commaSeparatedIntegerRe.test(value);
      }
    });
    Ext.apply(Ext.form.VTypes, {
        iPAddressText: Ext.form.field.Base.prototype.invalidText,
        iPAddressMask: /[\d\.]/,
        iPAddressRe: /^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$/,
        iPAddress: function(value){
            return Ext.form.VTypes.iPAddressRe.test(value);
      }
    });
});
