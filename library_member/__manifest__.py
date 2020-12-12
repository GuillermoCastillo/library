{ 
    'name': 'Library Members', 
    'summary' :'Manage library members',
    'description': 'Manage people who will be able to borrow books.', 
    'author': 'Guillermo Castillo', 
    'website' : 'www.critean.com',
    'depends': ['library_app','mail'], 
    'application': False, 
    #Version de la aplicación 
    'version': "13.0.1",
    'license':"LGPL-3",
    #Otros parametros
    'category': "Tools",
    'installable': True,
    'auto_install': False,
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',
    ],
}