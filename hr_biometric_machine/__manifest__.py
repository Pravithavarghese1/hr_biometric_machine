# -*- coding: utf-8 -*-
{
    'name': "Biometric Machine ",

    'summary': """
       Employee Attendance, Fingerprint Machine Integration""",

    'description': """
Biometric Machine Integration
=============================

This application enables you to integrate the fingerprint machine at you organization with Odoo.
Downloads the logs of each employee from the fingerprint machine with their details.
    """,

    'author': "Pravitha V",
    'website': "http://www.qpr.qa/",
    'category': 'Human Resources Custom',
    'version': '0.1',


<<<<<<< HEAD
    'depends': ['base_setup', 'hr', 'hr_attendance',],
=======
    'depends': ['base_setup', 'hr'],
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8


    'data': [
        # 'security/ir.model.access.csv',
        'views/biometric_machine_view.xml',
        'report/daily_attendance_view.xml',
        'schedule.xml',
        'wizard/schedule_wizard.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    
}