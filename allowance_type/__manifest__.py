# -*- coding: utf-8 -*-
{
    'name': "AllowanceTypes",
    'sequence': -100,
    'summary': """
        SALARY ALLOWANCE""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Atlas",
    'website': "http://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base','sale','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/allowance_type.xml',
        'views/hr_salary_info.xml',


    ],
    'installable': True,
    'application': True,
}
