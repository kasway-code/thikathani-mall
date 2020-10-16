# -*- coding: utf-8 -*-
{
    'name': "Modulo Ilo",

    'summary': """
        Agrega campos personalizados a los productos.""",

    'description': """
        Agrega campos personalizados a los productos.
    """,

    'author': "Kasway",
    'website': "http://thikathani.com.pe/conocenos/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
