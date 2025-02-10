# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from datetime import timedelta
from datetime import datetime


class Envio(models.Model):
    _name = 'quinto_wood.envio'
    _description = 'Quinto_wood Envio'

    direccion = fields.Text(string="Dirección", required=True, help="Dirección de envío")
    cpostal = fields.Integer(string="Código Postal", required=True, help="Código postal del envío")
    fechaEnvio = fields.Datetime(string="Fecha de envío", required=True, help="Fecha en la que se envió el envío")
    fechaLlegada = fields.Datetime(string="Fecha de llegada", help="Fecha en la que llegará el envío")
    estado = fields.Selection([('preparacion','En preparación'),
                                     ('enviado','Enviado'),
                                     ('entregado','Entregado')],
                                     'Estado del envío')


    venta_id = fields.Many2one('quinto_wood.venta', string="Ventas")

    @api.constrains('cpostal')
     def _check_cpostal(self):
          if self.cpostal > 5:
               raise models.ValidationError('El código postal debe ser de 5 dígitos.')
