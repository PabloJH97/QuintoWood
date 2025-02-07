# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Envio(models.Model):
    _name = 'quinto_wood.envio'
    _description = 'Quinto_wood Envio'

    direccion = fields.Text(string="Dirección", required=True, help="Dirección de envío")
    cpostal = fields.Integer(string="Código Postal", size=5 required=True, help="Código postal del envío")
    fechaEnvio = fields.Datetime(string="Fecha de envío", required=True, help="Fecha en la que se envió el envío")
    fechaLlegada = fields.Datetime(string="Fecha de llegada", help="Fecha en la que llegará el envío")
    estado = fields.Selection([('preparacion','En preparación'),
                                     ('enviado','Enviado'),
                                     ('entregado','Entregado')],
                                     'Estado del envío')


    venta_id = fields.Many2one('quinto_wood.venta', string="Ventas")
