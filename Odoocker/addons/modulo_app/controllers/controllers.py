# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloApp(http.Controller):
#     @http.route('/modulo_app/modulo_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_app/modulo_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_app.listing', {
#             'root': '/modulo_app/modulo_app',
#             'objects': http.request.env['modulo_app.modulo_app'].search([]),
#         })

#     @http.route('/modulo_app/modulo_app/objects/<model("modulo_app.modulo_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_app.object', {
#             'object': obj
#         })
