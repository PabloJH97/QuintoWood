# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Producto(models.Model):
    _name = 'quinto_wood.producto'
    _description = 'Quinto_wood Producto'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del producto")
    precio = fields.Float(string="Precio", required=True, help="Precio del producto")
    fecha_fabricacion = fields.Date(string="Fecha de Fabricación", help="Fecha en la que se fabricó el producto")
    pais = fields.Char(string="País de Origen", help="País donde se fabricó el producto")
    foto_producto = fields.Binary(string="Foto del Producto", help="Imagen del producto")
    proveedor_id = fields.Many2one('quinto_wood.proveedor', string="Proveedor", help="Proveedor del producto")
    venta_ids = fields.Many2many('quinto_wood.venta', string="Ventas")

#Validación de precio no negativo
@api.constrains('precio')
def _check_precio_no_negativo(self):
    for record in self:
       if record.precio < 0:
           raise ValidationError("El precio del producto no puede ser negativo.")