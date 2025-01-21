# -*- coding: utf-8 -*-
# from odoo import http


# class Rata(http.Controller):
#     @http.route('/rata/rata/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rata/rata/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rata.listing', {
#             'root': '/rata/rata',
#             'objects': http.request.env['rata.rata'].search([]),
#         })

#     @http.route('/rata/rata/objects/<model("rata.rata"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rata.object', {
#             'object': obj
#         })
