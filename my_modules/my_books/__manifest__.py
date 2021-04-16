# -*- coding: utf-8 -*-
{
    'name': "my_books",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
    """,
    'description': """
        Long description of module's purpose
    """,
    'author': "Authorized",
    'website': "https://erp.cloudmedia.vn",
    'category': 'Productivity',
    'version': '0.1',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'application': True,
    'demo': [
        'demo/demo.xml',
    ],
    'auth_install': False
}
