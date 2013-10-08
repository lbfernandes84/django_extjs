# encoding:utf-8
    
ListenersConfig = {
                   'doc': "Permite definir um listener para um componente que será renderizado no cliente. A função que liga o evento ao componente que deve estar em um arquivo javascript definido nos arquivos estáticos do Django",
                   'addListenerEvent': "Adiciona um atributo a um objeto estanciado da classe onde o nome do atributo será o nome do evento a ser chamado com o componente escolhido, esse atributo receberá uma tupla de dois componentes \
                        onde o primeiro será o nome da função javascript que irá disparar esse evento no cliente e o segundo os argumentos extras que serão adicionados a função. Caso um evento com um mesmo nome tiver sido inserido \
                        anteriormente ele não será adicionado para esse tipo de operação deve ser usado o metodo updateEventArguments",
                   'updateEventArguments': "Atualiza um evento adicionado anteriormente com novos dados, quando o evento a ser atualizado não existe é lançado um erro informando que aquele evento não existe",
                   'as_dict':"Converte os eventos adicionados como atributos da classe para um dicionário com um atributo único chamado 'listeners', esse dicionário será renderizado para o cliente no formato JSON como atributo do\
                       componente no qual foram definidos os eventos"
                  }

Item_Menu = {
             'doc':"Classe responsável por devolver um dicionário com configurações necessárias para criar um item de menu que será visualalizado na aplicação para chamar uma tela de listagem de um modelo, \
              Os seguintes argumentos são necessários a instanciação de um objeto:\n\
              - text: Texto do item de menu a ser vizualizado no cliente\n\
              - action: O nome da ação a ser tomada ao evento de clique no botão(É usado com padrões)\n\
              - title_window_list: Título da janela que será chamada pelo menu\n\
              - url_get_collumns: Url para a recuperação das colunas a serem inseridas na tela de listagem\n\
              - url_load_grid: Url para a recuperação dos itens mostrados na tela de listagem\n\
              - url_delete_record: Url para deletar itens da tela de listagem\n\
              - title_window_form: Título da janela de formulário ao adicionar ou editar um item da lista\n",
              "item_menu2dict": "Retorna um dicionário com atributos necessários para criação de um item de menu. Esse dicionário será serializado e passado ao cliente."
             }
Button = {
          "doc": "Implementa um botão que será renderizado no cliente nos padrões do Extjs. Recebe como atributos na instanciação os valores:\n\
              - label: Texto do botão que será utilizado\n\
              - action: Nome do evento que será disparado a clicarmos no botão\n\
              - path_image: Caminho relativo da imagem do botão\n\
              -tootip: Texto de ajuda que será disposto na tela quando o usuário passar o mouse sobre o botão",
          "get_configurations":"Retorna um dicionário com atributos necessários para criação de um botão. Esse dicionário será serializado e passado ao cliente."
          }
            
