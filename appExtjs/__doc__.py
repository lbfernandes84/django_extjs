# encoding:utf-8
    
ListenersConfig = {
                   'DOC': "Permite definir um listener para um componente que será renderizado no cliente. A função que liga o evento ao componente que deve estar em um arquivo javascript definido nos arquivos estáticos do Django",
                   'addListenerEvent': "Adiciona um atributo a um objeto estanciado da classe onde o nome do atributo será o nome do evento a ser chamado com o componente escolhido, esse atributo receberá uma tupla de dois componentes \
                        onde o primeiro será o nome da função javascript que irá disparar esse evento no cliente e o segundo os argumentos extras que serão adicionados a função. Caso um evento com um mesmo nome tiver sido inserido \
                        anteriormente ele não será adicionado para esse tipo de operação deve ser usado o metodo updateEventArguments",
                   'updateEventArguments': "Atualiza um evento adicionado anteriormente com novos dados, quando o evento a ser atualizado não existe é lançado um erro informando que aquele evento não existe",
                   'as_dict':"Converte os eventos adicionados como atributos da classe para um dicionário com um atributo único chamado 'listeners', esse dicionário será renderizado para o cliente no formato JSON como atributo do\
                       componente no qual foram definidos os eventos"
                  }
            
