# -*- encoding: utf-8 -*-

import setuptools
from os.path import join, dirname

setuptools.setup(
    name="django_extjs",
    version='0.0.1',
    packages=["appExtjs", "appExtjs/tests", "formExtjs","formExtjs/templatetags","formExtjs/tests", "gridExtjs", "gridExtjs/templatetags"],
    author="Joao Junior, Lucas Batista",
    author_email="joaojunior.ma@gmail.com, lbfernandes84@gmail.com",
    include_package_data=True,  # declarations in MANIFEST.in
    install_requires=open(join(dirname(__file__), 'requirements.txt')).readlines(),
    url="http://github.com/joaojunior/django_extjs",
    tests_require=[
        'django<1.5',
        'pil',
    ],
    license="Apache 2.0",
    description="Aplicacoes plugaveis django que ajuda a utilizar django com extjs",
    keywords="django extjs",
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)