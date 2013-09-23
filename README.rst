=================
Django Com Extjs
=================

Django com Extjs é um pacote com 3 aplicações: appExtjs, formExtjs e gridExtjs que permite utilizar o django junto com o extjs. 
Todas as três aplicações são aplicações django plugáveis. As aplicações formExtjs e gridExtjs podem ser usadas separadamente. A aplicação
appExtjs utiliza as aplicações formExtjs e gridExtjs.

O que faz?
==========
A aplicação formExtjs transforma um form django em um formulário do extjs. Ela trabalha identificando os tipos dos campos de um form django e
setando as propriedades correspondentes em um formulário do extjs, esse formulário é então retornado no formato json.
A aplicação gridExtjs é responsável por serializar os dados de um model do django para o formato aceito por um grid do extjs.
A aplicação appExtjs é uma aplicação MVC padrão do extjs. Com essa aplicação, após setar alguns propriedades, você terá um menu e as telas de listagens e
de CRUD em funcionamento em poucos instantes.

O que não faz?
==============

A aplicação appExtjs, apesar de criar uma aplicação quase pronta com telas de CRUD, não é uma bala de prata e com ela não acaba o problema 
de precisar escrever código. A intenção dessa aplicação é facilitar a construção de aplicações básicas que somente precisam de menus e CRUD´s simples.

Limitações Conhecidas
======================

Apenas datas no formato do Brasil são aceitas nessa versão.

Funcionalidades Interessantes utilizando a aplicação appExtjs:
===============================================================

.. [1] Os textos em uma busca, a partir de um grid do extjs, não são case-sensitive e não consideram a presença de acento.
.. [2] Em um grid extjs é possível pesquisar utilizando regex do python. 

Como instalar?
=======

pip install django_com_extjs

Configuração Básica:
====================

Após a instalação é preciso colocar as aplicações no INSTALLED_APPS do settings.py da sua aplicação. Assim:
.. code-block:: python
    INSTALLED_APPS = ( 'aqui está suas outras aplicações instaladas'
        'appExtjs',
        'formExtjs',
        'gridExtjs',)
Após isso é preciso informar ao django onde estão os arquivos estáticos dessas apps, assim:
.. code-block:: python
    from distutils.sysconfig import get_python_lib
    STATICFILES_DIRS = (
        os.path.join(get_python_lib(), 'appExtjs', 'static'),
        os.path.join(get_python_lib(), 'formExtjs', 'static'),
    )
Também é preciso informar ao django onde buscar o arquivo index.html da aplicação appExtjs, assim:
.. code-block:: python
    TEMPLATE_DIRS = ('aqui está o caminho dos seus outros templates'
        os.path.join(get_python_lib(), 'appExtjs', 'static'),
    )
Por último é necessário inserir as url´s nas urls da sua aplicação, assim:
.. code-block:: python
    urlpatterns = patterns('As suas outras urls estão aqui'
        (r'^appExtjs/', include('appExtjs.urls')),
        (r'^gridExtjs/', include('gridExtjs.urls')),
    )

Exemplos:
=========
Você pode obter um projeto de exemplo que mostra como utilizar a aplicação formExtjs e gridExtjs no endereço:
:target: https://github.com/joaojunior/poll_and_extjs
Apesar desse projeto utilizar as aplicações formExtjs e gridExtjs você pode olhar os html's e javascript's do endereço acima
para entender como juntar o django com o extjs.

Você pode obter um projeto de exemplo mostrando como se usa a aplicação appExtjs no endereço:
:target: https://github.com/joaojunior/example_appExtjs
