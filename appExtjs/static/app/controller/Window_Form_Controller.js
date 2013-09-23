Ext.define('AppExtjs.controller.Window_Form_Controller', {
    extend : 'Ext.app.Controller',
    views: ['Window_Form'],
    configuration : [],
    combo_for_update_after_save_new_value : null,
    init : function() {
        this.control({
            '[action=save]' : {
                click : this.save
            },
            '[action=add_model_child]' : {
                click : this.add_model_child
            },
            '[action=generate]':{
                click:this.generate
            }
        });
    },
    start_new_form : function(window_configuration,record){
        this.configuration = window_configuration;
        configurations_app = this.application.get_configurations();
		var id_url = "";
		if (typeof record.get != 'undefined'){
			id_url= record.get("pk");
		}
        Ext.Ajax.request({
            scope:this,
            method : 'GET',
            url: this.configuration.get_fields+id_url,
            params: {builder:'start_new_form' ,arguments:[window_configuration,record]},
            success: function (response) {
                var data;
                fields = this.buildFormFields(response.responseText);
                this.create_new_window(configurations_app,fields,record);
            },
            failure: function () {
                Ext.MessageBox.alert(configurations_app.ajax.failure.title,configurations_app.ajax.failure.msg);
            }
        });
    },
    create_new_window : function(configurations_app,fields) {
        var window_form = new Ext.create('AppExtjs.view.Window_Form',{configurations_app:configurations_app,
            configurations_window:this.configuration,'fields':fields,isReportForm:this.isReportForm(fields)});
        this.fit_windows(window_form);
        window_form.show();
    },
    fit_windows: function(window_form){
    	if (window_form.y < 0){
        	window_form.setHeight('80%');
			window_form.center();
		}
		window_form.setWidth('28%');
		window_form.down('form').setWidth('100%');
	},
    save : function(button) {
        var win = button.up('window');
        var form = win.down('form');
        if(form.getForm().isValid()){
            form.getForm().submit({
                scope: this,
                method:'POST',
                waitTitle:'Connecting',
                waitMsg:'Sending data...',
                params: {builder:'save' ,arguments:[button]},
                success: function(form, action){
                    win.close();
                    var window_list_controller = this.getController('Window_List_Controller');
                    this.update_widgets();
                    if(action.result.controller){
                        var controller = this.getController(action.result.controller.name);
                        eval('controller.' + action.result.controller.function_name);
                    };
                },
                failure: function(form, action){
                    dataReceived = Ext.decode(action.response.responseText);
                    message = dataReceived.messages
                    if(message){
                        Ext.MessageBox.alert('Failed',message);
                    };
                }
            });
        };
    },
    generate: function(button){
        var win = button.up('window');
        var form = win.down('form');
        form.getForm().standardSubmit=true;
        if(form.getForm().isValid()){
            form.getForm().submit({
                scope: this,
                method:'POST',
                       
             });
            //win.close();
        }
    },
    add_model_child : function(button){
        var win = button.up('window');
        var form = win.down('form');
        this.combo_for_update_after_save_new_value = form.getForm().findField(button.configuration.name_combo);
        var window_Form_Controller = this.getController('Window_Form_Controller');
        window_Form_Controller.start_new_form(button.configuration.form,{});
    },
    update_widgets:function(){
        if(this.combo_for_update_after_save_new_value){
            this.update_combo();
        }
        else{
            var window_list_controller = this.getController('Window_List_Controller');
            window_list_controller.refreshGrid();
        }
    },
    update_combo:function(){
        var combo = this.combo_for_update_after_save_new_value;
        combo.getStore().load();
        combo.expand(); 
        this.combo_for_update_after_save_new_value = null;
    },
    buildFormFields: function(responseText){
        var nonReadyFields = Ext.decode(responseText);
        Ext.Array.each(nonReadyFields,function(field,index){
            if (field.listeners){
                var newListeners = {};
                Ext.Object.each(field.listeners,function(listener){
                    newListeners[listener] = eval(field.listeners[listener]); 
                });
                field.listeners = newListeners; 
            }
        });
        return nonReadyFields;
    },
    isReportForm: function(fields){
        var isReportForm = false;
        Ext.Array.each(fields,function(field,index){
            if((field.xtype=='hiddenfield')&&(field.name=='reportForm')){
                isReportForm=true;
            }
        });
        return isReportForm;
    }
});