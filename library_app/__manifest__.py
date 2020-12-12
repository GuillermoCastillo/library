{
    'name': "Library Management",
    'summary': "Manage library catalogue",
    'description': 'Manage library book catalogue and lending.', 
    #datos de autor
    'author': 'Guillermo Castillo', 
    'website': "www.critean.com",
    'depends': ['base'], 
    'application': True, 
    #Version de la aplicación 
    'version': "13.0.1",
    'license':"LGPL-3",
    #otros parametros
    'category': "Tools",
    'installable': True,
    'auto_install': False,
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv', 
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
}