  # -*- encoding: utf-8 -*-
from django.conf import settings


class ListenersConfig(object):
    def addListenerEvent(self, eventName, functionName, **arguments):
        if not hasattr(self, eventName):
            setattr(self, eventName, (functionName, arguments))

    def updateEventArguments(self, eventName, **arguments):
        if hasattr(self, eventName):
            self.__dict__[eventName][1].update(arguments)
        else:
            raise AttributeError('Not added Event')

    def as_dict(self):
        listeners = {}
        for event, values in self.__dict__.items():
            listeners[event] = values[0]
            listeners[event + 'Options'] = values[1]
        return {'listeners':listeners}


class Menu_Exit(object):
    def __init__(self, text, action, link):
        self.text = text
        self.action = action
        self.link = link

    def item_menu_exit2dict(self):
        return {'text':self.text, 'action': self.action, 'link':self.link}


class Menu_Report(object):
    def __init__(self, text, action, link):
        self.text = text
        self.action = action
        self.link = link

    def item_menu_exit2dict(self):
        return {'text':self.text, 'action': self.action, 'link':self.link}


class Menu(object):
    DEFAULT_SUFFIX = 'Menu'

    def __init__(self, text, items_menu):
        self.text = text
        self.items_menu = items_menu
        textWithoutSpaces = text.replace(' ', '')
        self.cls = ''.join([textWithoutSpaces, self.DEFAULT_SUFFIX])

    def menu2dict(self):
        menu = {}
        menu['text'] = self.text
        menu['cls'] = self.cls
        items = []
        for item_menu in self.items_menu:
            items.append(item_menu.item_menu2dict())
        menu['menu'] = {'items':items}
        return menu


class Item_Menu(object):
    DEFAULT_SUFFIX = 'ItemMenu'

    def __init__(self, text, action, title_window_list, url_get_collumns, url_load_grid, url_delete_record, title_window_form,
        url_get_fields, url_save_record, url_report_record='', report_button_hidden=True):
        self.text = text
        self.action = action
        self.title_window_list = title_window_list
        self.url_get_collumns = url_get_collumns
        self.url_load_grid = url_load_grid
        self.url_delete_record = url_delete_record
        self.title_window_form = title_window_form
        self.url_get_fields = url_get_fields
        self.url_save_record = url_save_record
        self.url_report_record = url_report_record
        self.report_button_hidden = report_button_hidden
        textWithoutSpaces = text.replace(' ', '')
        self.cls = ''.join([textWithoutSpaces, self.DEFAULT_SUFFIX])

    def item_menu2dict(self):
        dict_item_menu = {'text':self.text, 'action': self.action, 'cls':self.cls, 'window_configuration':{
            'list':{'title':self.title_window_list, 'get_columns':self.url_get_collumns, 'url_load_grid':self.url_load_grid, 'delete_record':self.url_delete_record, 'report_url': self.url_report_record, 'report_button_hidden': self.report_button_hidden},
            'form':{'title':self.title_window_form, 'get_fields':self.url_get_fields, 'save_record':self.url_save_record}}}
        return dict_item_menu


class Button(object):
    DEFAULT_SUFFIX = 'Button'

    def __init__(self, action, label, path_image, tooltip):
        self.action = action
        self.label = label
        self.path_image = path_image
        self.tooltip = tooltip
        self.cls = ''.join([self.label, self.DEFAULT_SUFFIX])

    def get_configurations(self):
        return {'label':self.label, 'path_image':self.path_image, 'tooltip':self.tooltip, 'cls':self.cls}

    def button2dict(self):
        return {self.action:self.get_configurations()}


class Action(object):
    def __init__(self, action, title, msg):
        self.action = action
        self.title = title
        self.msg = msg

    def get_configurations(self):
        return {'title':self.title, 'msg':self.msg}

    def action2dict(self):
        return {self.action:self.get_configurations()}


class Ajax(object):
    def __init__(self, failure, title, msg):
        self.type_msg = failure
        self.title = title
        self.msg = msg

    def get_configurations(self):
        return {'title':self.title, 'msg':self.msg}

    def ajax2dict(self):
        return {self.type_msg:self.get_configurations()}


class Configuration_Initial(object):
    APP_TITLE = 'APP_TITLE' # nome da aplicação que será exibida em todas as telas do extjs
    APP_VERSION = '0.0.1' # número da verão da aplicaçãoo que será exibida na barra de status da aplicação extjs
    VERSION_LABEL = 'Versão:'
    BUTON_ADD_LABEL = 'Adicionar' #Label do botão add para ser exibido no extjs
    BUTTON_ADD_PATH_IMAGE = settings.STATIC_URL + 'imagens/add.png' #Caminho da imagem do botão add, para ser exibida no botão extjs
    BUTON_ADD_TOOLTIP = '' # mensagem de ajuda para ser exibido no extjs quando parar o mouse em cima do botão
    BUTON_DEL_LABEL = 'Remover'
    BUTTON_DEL_PATH_IMAGE = settings.STATIC_URL + 'imagens/delete.png'
    BUTON_DEL_TOOLTIP = ''
    BUTON_SAVE_LABEL = 'Salvar'
    BUTTON_SAVE_PATH_IMAGE = ''
    BUTON_SAVE_TOOLTIP = ''
    BUTON_CANCEL_LABEL = 'Cancelar'
    BUTTON_CANCEL_PATH_IMAGE = ''
    BUTON_CANCEL_TOOLTIP = ''
    BUTTON_REPORT_LABEL = 'Exportar'
    BUTTON_REPORT_PATH_IMAGE = settings.STATIC_URL + 'imagens/report.png'
    BUTTON_REPORT_TOOLTIP = ''
    ACTION_DELETE = 'delete_' # nome da ação extjs que será chamada
    ACTION_DELETE_TITLE = 'Confirmação' #título da tela de messagebox para confirmação de exclusão
    ACTION_DELETE_MSG = 'Você tem certeza que deseja excluir o registro selecionado?' #Mensagem de confirmação que será exibida no combobox
    AJAX_FAILURE = 'failure' # nome para toda exceção ajax que ocorrer
    AJAX_FAILURE_TITLE = 'Erro' # Título do messagebox que será exibido toda vez que ocorrer um erro em uma requisição ajax
    AJAX_FAILURE_MSG = 'Mensagem' # Mensagem que será exibida no messagebox toda vez que ocorrer um erro em uma requisição ajax
    ALLOW_REPORTS = False # flag que permite ou nao a criacao de relatorios dinamicos no sistema
    MENU_REPORT_TITLE = 'Relatórios'#Texto a ser exibido no menu de relatorios da toolbar
    MENU_REPORT_ACTION = 'report'#nome da ação extjs que será chamada quando usuario clicar no botao
    MENU_REPORT_URL = '/'#URL que o menu de relatorios irá
    MENU_EXIT_TITLE = 'Sair'#Texto a ser exibido no menu de saída/logou da toolbar
    MENU_EXIT_ACTION = 'exit'#nome da ação extjs que será chamada 
    MENU_EXIT_URL = '/'#URL que o menu de saída irá
    DELETE_SUCESS_TITLE = 'Exclusão'#Título do messagebox que será exibido após exlcuir o registro
    DELETE_SUCESS_MSG = 'Registro removido com sucesso.'#Mensagem que será exibida no messagebox após exluir o registro
    DELETE_EXCEPT_PROTECTED_ERROR_MSG = u'O registro não pode ser removido, pois ele é referencia direta para [%s] de %s, remova primeiro esses registros.'

    def __init__(self, menus=[]):
        self.configurations = {'success':True}
        self.configurations['application'] = {'title' : self.APP_TITLE, 'version':{'title':self.VERSION_LABEL + self.APP_VERSION, 'number':self.APP_VERSION}}
        self.menus = menus

    def configuration_Initial2dict(self):
        try:
            self.configurations = {"success": True}
            self.configurations['application'] = {'title' : self.APP_TITLE, 'version':{'title':self.VERSION_LABEL + self.APP_VERSION, 'number':self.APP_VERSION}}
            button_add = Button('add', self.BUTON_ADD_LABEL, self.BUTTON_ADD_PATH_IMAGE, self.BUTON_ADD_TOOLTIP)
            button_del = Button('del', self.BUTON_DEL_LABEL, self.BUTTON_DEL_PATH_IMAGE, self.BUTON_DEL_TOOLTIP)
            button_save = Button('save', self.BUTON_SAVE_LABEL, self.BUTTON_SAVE_PATH_IMAGE, self.BUTON_SAVE_TOOLTIP)
            #button_login = Button('login', self.BUTON_LOGIN_LABEL, self.BUTTON_LOGIN_PATH_IMAGE, self.BUTON_LOGIN_TOOLTIP)
            button_cancel = Button('cancel', self.BUTON_CANCEL_LABEL, self.BUTTON_CANCEL_PATH_IMAGE, self.BUTON_CANCEL_TOOLTIP)
            button_report = Button('report', self.BUTTON_REPORT_LABEL, self.BUTTON_REPORT_PATH_IMAGE, self.BUTTON_REPORT_TOOLTIP)
            buttons = {button_add.action :button_add.get_configurations(),
                    button_del.action :button_del.get_configurations(),
                    button_save.action :button_save.get_configurations(),
                    #button_login.action :button_login.get_configurations(),
                    button_cancel.action :button_cancel.get_configurations(),
                    button_report.action: button_report.get_configurations()}
            action_delete = Action(self.ACTION_DELETE, self.ACTION_DELETE_TITLE, self.ACTION_DELETE_MSG)
            actions = {action_delete.action:action_delete.get_configurations()}
            ajax = Ajax(self.AJAX_FAILURE, self.AJAX_FAILURE_TITLE, self.AJAX_FAILURE_MSG)
            ajax = {ajax.type_msg:ajax.get_configurations()}
            if self.ALLOW_REPORTS:
                self.menu_reports = Menu_Report(self.MENU_REPORT_TITLE, self.MENU_REPORT_ACTION, self.MENU_REPORT_URL)
            self.menu_exit = Menu_Exit(self.MENU_EXIT_TITLE, self.MENU_EXIT_ACTION, self.MENU_EXIT_URL)
            menus = self.menus2list()
            self.configurations['button'] = buttons
            self.configurations['actions'] = actions
            self.configurations['ajax'] = ajax
            self.configurations['menu'] = menus
        except:
            self.configurations = {'success':False}
            self.configurations['title'] = 'Erro'
            self.configurations['msg'] = 'Nao foi possivel carregar os dados do menu'
        return self.configurations

    def menus2list(self):
        menus = []
        for menu in self.menus:
            menus.append(menu.menu2dict())
        if self.ALLOW_REPORTS:
            menus.append(self.menu_reports.item_menu_exit2dict())
        menus.append('->')
        menus.append('-')
        menus.append(self.menu_exit.item_menu_exit2dict())
        return menus


class ConfigurationInitialTest(Configuration_Initial):
    def __init__(self, *args, **kwargs):
        menuFather = self.__getMenuFather()
        menuTest = self.__getMenuTest()
        menuFormset = self.__getMenuPaiFormset()
        kwargs['menus'] = [menuFather, menuTest, menuFormset]
        super(ConfigurationInitialTest, self).__init__(*args, **kwargs)

    def __getMenuFather(self):
        parametersMenu = {}
        parametersMenu['text'] = 'Novo'
        parametersMenu['action'] = 'click_menu'
        parametersMenu['title_window_list'] = 'Father'
        parametersMenu['url_get_collumns'] = 'test/get_columns/Father/'
        parametersMenu['url_load_grid'] = 'test/load_grid/Father/'
        parametersMenu['url_delete_record'] = 'test/delete/Father/'
        parametersMenu['title_window_form'] = 'Father'
        parametersMenu['url_get_fields'] = 'test/get_fields/Father/'
        parametersMenu['url_save_record'] = 'test/save_form/Father/'
        itemMenu = Item_Menu(**parametersMenu)
        menu = Menu('Father', [itemMenu])
        return menu

    def __getMenuTest(self):
        parametersMenu = {}
        parametersMenu['text'] = 'Novo'
        parametersMenu['action'] = 'click_menu'
        parametersMenu['title_window_list'] = 'Modelo de Teste'
        parametersMenu['url_get_collumns'] = 'test/get_columns/ModeloParaTeste/'
        parametersMenu['url_load_grid'] = 'test/load_grid/ModeloParaTeste/'
        parametersMenu['url_delete_record'] = 'test/delete/ModeloParaTeste/'
        parametersMenu['title_window_form'] = 'Modelo de Teste'
        parametersMenu['url_get_fields'] = 'test/get_fields/FormTeste/'
        parametersMenu['url_save_record'] = 'test/save_form/FormTeste/'
        itemMenu = Item_Menu(**parametersMenu)
        menu = Menu('Modelo de Teste', [itemMenu])
        return menu

    def __getMenuPaiFormset(self):
        parametersMenu = {}
        parametersMenu['text'] = 'Pai'
        parametersMenu['action'] = 'click_menu'
        parametersMenu['title_window_list'] = 'Test Formset'
        parametersMenu['url_get_collumns'] = 'testformset/get_columns/PaiToFormset/'
        parametersMenu['url_load_grid'] = 'testformset/load_grid/PaiToFormset/'
        parametersMenu['url_delete_record'] = 'testformset/delete/PaiToFormset/'
        parametersMenu['title_window_form'] = 'Pai Formset'
        parametersMenu['url_get_fields'] = 'testformset/get_fields/PaiToFormset/'
        parametersMenu['url_save_record'] = 'testformset/save_form/PaiToFormset/'
        itemMenu = Item_Menu(**parametersMenu)
        menu = Menu('PaiToFormset', [itemMenu])
        return menu

class FunctionJavaScript(object):
    def __init__(self, function_name, function_parameters=None):
        self.function_name = function_name
        self.function_parameters = function_parameters

    def as_dict(self):
        if self.is_with_parameters():
            parameters = self.values_in_dict_to_list_string()
            parameters = self.list_to_string_join(parameters)
            return {'function_name':'%s(%s)' % (self.function_name, parameters)}
        else:
            return {'function_name':'%s()' % self.function_name}

    def is_with_parameters(self):
        return self.function_parameters

    def values_in_dict_to_list_string(self):
        parameters = self.function_parameters.values()
        for index, parameter in enumerate(parameters):
            parameters[index] = str(parameter)
        return parameters

    def list_to_string_join(self, parameters):
        return ','.join(parameters)

