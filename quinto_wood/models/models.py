# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class quinto_wood(models.Model):
#     _name = 'quinto_wood.quinto_wood'
#     _description = 'quinto_wood.quinto_wood'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
