Ext.define('AppExtjs.view.Viewport', {
    extend: 'Ext.container.Viewport',
    version : {},
    menu : [],
    constructor : function(options){
        Ext.apply(this,options || {});
        this.callParent();
    },
	requires: ['AppExtjs.view.StatusBar','AppExtjs.view.Content'],
	layout: 'fit',
    initComponent: function() {
        this.items = {
            xtype: 'panel',
            dockedItems: [{
                dock: 'top',
                xtype: 'toolbar',
                height: 30,
                items : this.menu
            },{
                dock: 'bottom',
                xtype: 'toolbar',
                height: 20,
                items: [{
                    xtype: 'statusBar',
                    flex: 1
                },
                {
                  xtype: 'box',
                  autoEl: {cn: this.version.title}
                }]
            }],
             layout: {
                type: 'hbox',
                align: 'stretch'
            },
            items: [{
                flex: 1,
                xtype: 'content',
                layout: {
                    type: 'vbox',
                    align: 'stretch'
                }
            }]
        };
        this.callParent();
    }
});

