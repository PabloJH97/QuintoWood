# -*- coding: utf-8 -*-
{
    'name': "Quintowood",

    'summary': """
       Aplicación de Odoo para una fábrica de madera """,

    'description': """
        Aplicación de Odoo para gestionar una fábrica de madera 
    """,

    'author': "Almudena Vega, Alejandro Bueno y Pablo Hurtado",
    'website': "http://www.quintowood.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application' : True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/persona_view.xml',
        'views/cliente_view.xml',
        'views/empleado_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
