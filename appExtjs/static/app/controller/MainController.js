Ext.define('AppExtjs.controller.MainController', {
	extend : 'Ext.app.Controller',
	views : ['AppExtjs.view.Viewport'],
	lastMenuConfiguration : null,
	init : function() {
		this.control({
			'toolbar [action=click_menu]' : {
				click : this.click_menu
			},
            'toolbar [action=exit]' : {
				click : this.exit
			},
            'toolbar [action=report]' : {
				click : this.relatorios
			},
			'toolbar [action=chart]' :{
				click: this.chart
			}
		});
	},
	click_menu : function(menu) {
        this.lastMenuConfiguration = menu.window_configuration;
		var window_List_Controller = this.getController('Window_List_Controller');
        window_List_Controller.start_new_window_list(menu.window_configuration);
	},
    exit : function(menu){
        this.redirect_init();
    },
	redirect_init: function(){
		window.location = '/'
	},
    start_app : function(){
        Ext.Ajax.request({
            scope:this,
            method : 'GET',
            url: 'get_configurations_initial/',
            params:{builder:'start_app' ,arguments:[]},
            success: function (response) {
                var data;
                data = Ext.decode(response.responseText);
                if (data.success === true) {
					this.application.set_configurations(data);
                    var viewport = Ext.create('AppExtjs.view.Viewport',{menu:data.menu,version:data.application.version});
                } 
				else{
					Ext.MessageBox.alert(data.title, data.msg);
				}
            },
            failure: function () {
                Ext.MessageBox.alert(configurations_app.ajax.failure.title,configurations_app.ajax.failure.msg);
            }
        });
    },
	relatorios: function(menu){
		var reportController = this.getController('Window_Report_Controller');
        reportController.start_new_Report(menu.window_configuration);
	},
	chart: function(menu){
		var chartController = this.getController('Window_Chart_Controller');
        chartController.start_new_Chart(menu.window_configuration);
	}
});