# -*- coding: utf-8 -*-
# from odoo import http


# class Banco(http.Controller):
#     @http.route('/banco/banco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/banco/banco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('banco.listing', {
#             'root': '/banco/banco',
#             'objects': http.request.env['banco.banco'].search([]),
#         })

#     @http.route('/banco/banco/objects/<model("banco.banco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('banco.object', {
#             'object': obj
#         })
