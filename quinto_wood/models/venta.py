# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Venta(models.Model):
    _name='quinto_wood.venta'
    _description='Quinto_wood Venta'

    idVenta = fields.Integer(string="Id Venta", readonly=True, help="Id de la venta")
    fecha = fields.Datetime(string="Fecha", required=True, help="Fecha de la venta")
    enviogratis = fields.Boolean(string="Envio Gratis", required=True, help="¿Envío gratis?")
    precioTotal = fields.Float(string="Precio Total", readonly=True, compute='_compute_precio_total', store=True, help="Precio Total")

    envio_id = fields.Many2one('quinto_wood.envio', string="Envío")
    producto_id = fields.Many2many('quinto_wood.producto', string="Productos")
    cliente_id = fields.Many2one('quinto_wood.cliente', string="Clientes")
    empleado_id = fields.Many2one('quinto_wood.empleado', string="Empleados")
    
    @api.model
    def create(self, vals):
        record = super(Venta, self).create(vals)
        
        record.idVenta=record.id

        return record
    
    @api.depends('producto_id', 'enviogratis')
    def _compute_precio_total(self):
        for venta in self:

            if venta.enviogratis:
                venta.precioTotal=0.0
            else:
                total = 0.0
                for producto in venta.producto_id:
                    precio=producto.precio
                    total+=precio

                venta.precioTotal=total



