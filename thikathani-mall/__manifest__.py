# -*- coding: utf-8 -*-
{
    'name': "ThikaThani",

    'summary': """
        Agrega campos personalizados y nuevos modelos dirigidos a ThikaThani Mall.
    """,

    'description': """
        Agrega campos personalizados y nuevos modelos dirigidos a ThikaThani Mall.
    """,

    'author': "Kasway",
    'website': "http://thikathani.com.pe/conocenos/",

    'category': 'Sales',
    'version': '0.2',

    'depends': [
        'base',
        'sale',
        'stock'
    ],

    'data': [
        'views/product_brand_views.xml',
        'views/product_template_views.xml',
        'security/ir.model.access.csv',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
}
