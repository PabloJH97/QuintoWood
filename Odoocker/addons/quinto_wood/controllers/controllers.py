# -*- coding: utf-8 -*-
# from odoo import http


# class QuintoWood(http.Controller):
#     @http.route('/quinto_wood/quinto_wood/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quinto_wood/quinto_wood/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quinto_wood.listing', {
#             'root': '/quinto_wood/quinto_wood',
#             'objects': http.request.env['quinto_wood.quinto_wood'].search([]),
#         })

#     @http.route('/quinto_wood/quinto_wood/objects/<model("quinto_wood.quinto_wood"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quinto_wood.object', {
#             'object': obj
#         })
