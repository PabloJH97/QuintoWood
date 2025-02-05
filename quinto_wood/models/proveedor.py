# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Proveedor(models.Model):
    _name = 'quinto_wood.proveedor'
    _description = 'Quinto_wood Proveedor'

    nombre = fields.Char(String = "Nombre",required=True, help="Nombre del proveedor")
    cif = fields.Char(String = "CIF", required= True,help = "CIF del proveedor")
    direccion = fields.Char(String = "Direccion")
    logo = fields.Binary(String = "Logo")
    telefono = fields.Integer(String = "Telefono")
    productos_id = fields.One2many('quinto_wood.producto', 'proveedor_id', string="Productos")

#Validación de CIF único
@api.constrains('cif')
def _check_cif_unico(self):
    for record in self:
        existing_proveedor = self.search([('cif', '=', record.cif), ('id', '!=', record.id)])
        if existing_proveedor:
            raise ValidationError("El CIF debe ser único. Ya existe un proveedor con este CIF.")
     