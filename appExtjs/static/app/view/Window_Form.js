Ext.define('AppExtjs.view.Window_Form' ,{
    extend: 'Ext.window.Window',
    alias : 'widget.window_Form',
    configurations_app : [],
    configurations_window :[],
    fields : [],
    title : '',
    layout: 'fit',
    autoShow: true,
    autoScroll: true,
    maximizable : true,
    isReportForm:false,
    constructor:function(options){
        Ext.apply(this,options || {});
        this.title = this.configurations_window.title;
        this.callParent(arguments);
    },
    initComponent: function() {
        this.fields.push({'xtype': 'hiddenfield','name': 'csrfmiddlewaretoken','value':Ext.util.Cookies.get('csrftoken')});//Isso é necessário para fazer upload de arquivo
        this.items = [
            {
                xtype: 'form',
                frame:true,
                fileUpload: true,
                url:this.configurations_window.save_record,
                items: this.fields,
                autoScroll : true
            }
        ];
        if (!this.isReportForm){
            this.buttons = [
                {
                    text: this.configurations_app.button.save.label,
                    action: 'save',
                    cls: this.configurations_app.button.save.cls
                },
                {
                    text: this.configurations_app.button.cancel.label,
                    scope: this,
                    handler: this.close,
                    cls: this.configurations_app.button.cancel.cls
                }
            ];
        }
        else{
            this.buttons = [
                {
                    text: 'Gerar',
                    action: 'generate',
                }
            ];
        }

        this.callParent(arguments);
    }	
});