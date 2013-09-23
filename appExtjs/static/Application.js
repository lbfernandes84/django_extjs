Ext.Loader.setConfig({enabled: true});
Ext.Loader.setPath({'Ext':prefix_path + 'extjs/src'});
Ext.Loader.setPath({'Ext.ux':prefix_path + 'extjs/examples/ux'});
Ext.require(
    ['Ext.form.field.Date', 'Ext.form.Panel','Ext.ux.grid.FiltersFeature', 'Ext.view.*', 'Ext.grid.header.Container']
);

Ext.require(["Ext.util.Cookies", "Ext.Ajax"], function(){
    //Add csrf token to every ajax request
	var token = Ext.util.Cookies.get('csrftoken');
	if(token){
		Ext.Ajax.defaultHeaders = Ext.apply(Ext.Ajax.defaultHeaders || {}, {
			'X-CSRFToken': token
		});
	}
});

Ext.application({
    name: 'AppExtjs',
    appFolder: prefix_path + 'app',
    configurations : [],
    sessionId : null,
	controllers : ['Window_List_Controller',
	               'MainController',
				   'Window_Form_Controller',
				   'Window_Report_Controller'],
    launch: function() {
        var mainController = this.getController('AppExtjs.controller.MainController');
		mainController.start_app();
    },
    get_configurations: function(){
        return this.configurations;
    },
    set_configurations: function(configurations){
        this.configurations = configurations;
    }
});