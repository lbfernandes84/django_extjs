Ext.define('AppExtjs.controller.Window_List_Controller', {
	extend : 'Ext.app.Controller',
    views: ['Window_List'],
    window_list : null,
	permissions:null,
    configuration : [],
	init : function() {
        this.control({
			'toolbar [action=add_model]' : {
				click : this.add_model
			},
            'toolbar [action=delete_model]' : {
				click : this.delete_model
			},
            'toolbar [action=report_model]' : {
				click : this.report_model
			},
            '[xtype="gridpanel"]' : {
				itemdblclick: this.edit_model
			}
		});
	},
    start_new_window_list : function(window_configuration){
        configurations_app = this.application.get_configurations();
        this.configuration = window_configuration;
        Ext.Ajax.request({
            params: {builder:'start_new_window_list' ,arguments:[window_configuration]},
            scope:this,
            method : 'GET',
            url: window_configuration.list.get_columns,
            success: function (response) {
                var data;
                data = Ext.decode(response.responseText);
				this.permissions=data.permissions;
				this.create_new_window(configurations_app,data.columns);
                },
            failure: function () {
                Ext.MessageBox.alert(configurations_app.ajax.failure.title,configurations_app.ajax.failure.msg);
            }
        });
    },
    create_new_window : function(configurations_app,columns) {
		overrides = {}
        var window_list = new Ext.create('AppExtjs.view.Window_List',{configurations_app:configurations_app,
            configurations_window:this.configuration.list,columns:columns});
        this.window_list = window_list;
        this.window_list.show();
	},
    add_model : function(menu){
        var window_Form_Controller = this.getController('Window_Form_Controller');
        window_Form_Controller.start_new_form(this.configuration.form,{});
	},
    edit_model : function(grid, record){
        var window_Form_Controller = this.getController('Window_Form_Controller');
        window_Form_Controller.start_new_form(this.configuration.form,record);
    },
    delete_model : function(menu) {
        var grid = this.window_list.down('gridpanel');
        var line = grid.getSelectionModel().getSelection();
        configurations_app = this.application.get_configurations();
        if(line[0] != null){
            var record = grid.getView().getSelectionModel().getSelection()[0];
            Ext.MessageBox.confirm(configurations_app.actions.delete_.title, configurations_app.actions.delete_.msg,function(btn){
                if (btn.toUpperCase()==Ext.MessageBox.msgButtons['yes'].text.toUpperCase()){
                    Ext.Ajax.request({
                        scope:this,
                        method : 'POST',
                        url: this.configuration.list.delete_record + record.data.pk + '/',
                        params: {builder:'delete_model' ,arguments:[menu]},
                        success: function (response) {
                            var data;
                            data = Ext.decode(response.responseText);
                            Ext.MessageBox.alert(data.title, data.msg);
                            if (data.success == true) {
                                this.refreshGrid();
                            };
                        },
                        failure: function () {
                            Ext.MessageBox.alert(configurations_app.ajax.failure.title,configurations_app.ajax.failure.msg);
                        }
                    });
                };
            },this);
        };
	},
	report_model: function(menu){
		var grid = this.window_list.down('gridpanel');
        var sorters = this.getSortersOfSort(grid.store);
        var filters = this.getFiltersOfGrid(grid);
        //Aqui Esta assim pois nao conseguimos fazer uma chamada Ajax para retornar o download de um arquivo
        window.location = this.configuration.list.report_url+'?'+sorters + filters;
	},
    getSortersOfSort:function(store){
        var sorters = "sort=" + Ext.JSON.encode(store.sorters.items);
        return sorters;
    },
    getFiltersOfGrid:function(grid){
        var filterData = grid.filters.getFilterData();
        var filterQuery = grid.filters.buildQuery(filterData);
        var filters ="";
        Ext.each(filterQuery, function(item){
            for(var key in item) {
                filters = filters + "&" + key + "=" + item[key];
               }
        });
        return filters;
    },
    refreshGrid:function(){
		var grid = this.window_list.down('gridpanel');
        grid.getStore().load();
    }
});