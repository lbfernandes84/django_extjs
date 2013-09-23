Ext.define('AppExtjs.controller.Window_Report_Controller', {
	extend : 'Ext.app.Controller',
    views: ['Window_Report'],
    configuration : [],
    start_new_Report : function(window_configuration){
        this.configuration = window_configuration;
        configurations_app = this.application.get_configurations();
		this.create_new_window(configurations_app);
    },
    create_new_window : function(configurations_app) {
        var window_report = new Ext.create('AppExtjs.view.Window_Report',{configurations_app:configurations_app,
            configurations_window:this.configuration});
		var dropTarget = new Ext.dd.DDTarget(Ext.getCmp('dropArea'),'gridColumnDD');
        window_report.show();
	}
});