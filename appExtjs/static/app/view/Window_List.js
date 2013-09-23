
Ext.define('AppExtjs.view.Window_List' ,{
    extend: 'Ext.window.Window',
    alias : 'widget.window_List',
    title : '',
    configurations_app : [],
    configurations_window : [],
    columns : [],
    layout: 'fit',
    width   : '80%',
    height   : '80%',
    autoShow: true,
    resizable: true,
    maximizable : true,  
    constructor:function(options){
        Ext.apply(this,options || {});
        this.title = this.configurations_app.application.title;
        this.callParent(arguments);
    },
    initComponent: function() {
        var fields = new Array();
        for (object in this.columns){
            fields.push(this.columns[object].dataIndex);
        };
        var store = Ext.create('Ext.data.Store', {
            remoteSort: true,
			remoteFilter: true,
            autoLoad: true,
            scope:this,
            pageSize: 25,
            proxy: {
                type: 'ajax',
                url: this.configurations_window.url_load_grid,
                reader: {
                    type: 'json',
                    root: 'register',
                    totalProperty: 'total'
                }
            },
            fields:fields
        });
    
	   var filters = {
	        ftype: 'filters'
       };
      var groupingFeature =  Ext.create('Ext.grid.feature.Grouping',{
        groupHeaderTpl: 'Campo: {name} ({rows.length} Item{[values.rows.length > 1 ? "s" : ""]})'});
        this.dockedItems =  [{
            xtype: 'toolbar',
            items : [{
                xtype: 'button',
                id: Ext.id(),
                name: "add",
                icon: this.configurations_app.button.add.path_image,
                text: this.configurations_app.button.add.label,
                tooltip: this.configurations_app.button.add.tooltip,
				cls: this.configurations_app.button.add.cls,
                action: 'add_model',
                scope: this
            },
			{
                xtype: 'button',
                id: Ext.id(),
                name: "del",
                icon: this.configurations_app.button.del.path_image,
                text: this.configurations_app.button.del.label,
                tooltip: this.configurations_app.button.del.tooltip,
				cls: this.configurations_app.button.del.cls,
                action: 'delete_model',
                scope: this
            },
			{
				xtype: 'button',
                name: "export",
				id: Ext.id(),
				icon: this.configurations_app.button.report.path_image,
				text: this.configurations_app.button.report.label,
				tooltip: this.configurations_app.button.report.tooltip,
				cls: this.configurations_app.button.report.cls,
                action: 'report_model',
                scope: this,
				hidden: this.configurations_window.report_button_hidden
			}
            ]
        }];
    
        
        this.items = [{
                xtype: 'gridpanel',
				autoRender:true,
                store: store,
				features: [groupingFeature,filters],
                columns: this.columns,
                stateful:false,
                stateId:'stateGrid',
				id: Ext.id(),
                height: '95%',
                width: '100%',
				loadMask: true,
                title: this.configurations_window.title,
                viewConfig: {
                    stripeRows: true
                },
                dockedItems: [{
                    xtype: 'pagingtoolbar',
                    store: store,   // same store GridPanel is using
                    dock: 'bottom',
                    displayInfo: true
                }]
            }
        ];
        this.callParent(arguments);
    }
});