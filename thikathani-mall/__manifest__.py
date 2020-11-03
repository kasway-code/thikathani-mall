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
        'stock',
    ],

    'data': [
        'security/ir.model.access.csv',
    ],

    'application': True,
    'installable': True,
}
