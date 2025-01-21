# -*- coding: utf-8 -*-
{
    'name': "library",

    'summary': """
       Aplicación de Odoo para gestionar una biblioteca """,

    'description': """
        Aplicación de Odoo para gestionar una biblioteca
    """,

    'author': "2DAM",
    'website': "http://www.ieshnosmachado.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application' : True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/menu_view.xml', # despues de otras vistas
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
