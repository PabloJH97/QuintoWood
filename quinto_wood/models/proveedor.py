# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Proveedor(models.Model):
    _name = 'quinto_wood.proveedor'
    _description = 'Quinto_wood Proveedor'

    nombre = fields.Char(String = "Nombre",required=True, help="Nombre del proveedor")
    cif = fields.Char(String = "CIF", required= True,help = "CIF del proveedor")
    direccion = fields.Char(String = "Direccion")
    logo = fields.Binary(String = "Logo")
    telefono = fields.Integer(String = "Telefono")
    productos_id = fields.One2many('quinto_wood.producto', 'proveedor_id', string="Productos")
     