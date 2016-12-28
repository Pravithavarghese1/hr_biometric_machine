# -*- coding: utf-8 -*-
from odoo import http

# class HrBiometricMachine(http.Controller):
#     @http.route('/hr_biometric_machine/hr_biometric_machine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_biometric_machine/hr_biometric_machine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_biometric_machine.listing', {
#             'root': '/hr_biometric_machine/hr_biometric_machine',
#             'objects': http.request.env['hr_biometric_machine.hr_biometric_machine'].search([]),
#         })

#     @http.route('/hr_biometric_machine/hr_biometric_machine/objects/<model("hr_biometric_machine.hr_biometric_machine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_biometric_machine.object', {
#             'object': obj
#         })