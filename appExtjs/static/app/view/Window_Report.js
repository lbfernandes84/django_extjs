Ext.define('AppExtjs.view.Window_Report' ,{
    extend: 'Ext.window.Window',
    alias : 'widget.window_Report',
    configurations_app : [],
    configurations_window :[],
    title : '',
    layout: 'border',
    autoShow: true,
	width: '75%',
	height: '75%',
    maximizable : true,
    constructor:function(options){
        Ext.apply(this,options || {});
        this.title = 'Reports';
        this.callParent(arguments);
    },
    initComponent: function() {
        this.items = [
            {
				id: 'dropArea',
				title: 'Report Parameters',
				region: 'west',
				width: '25%',
				split: true,
				collapsible: true,
				floatable: false,
                listeners: {
					   drop: function(node, data, dropRec, dropPosition) {
					   	alert('teste');
				      }
    		    } 
            },
			{
				region: 'center',
				xtype: 'tabpanel'
			}
        ];

        this.buttons = [
            {
                text: this.configurations_app.button.cancel.label,
                scope: this,
                handler: this.close
            }
        ];

        this.callParent(arguments);
    }	
});