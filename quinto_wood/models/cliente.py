# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = 'persona.cliente' # modulo.modelo
    _inherit= 'quintowood.persona'
    _description = 'Un cliente'

    direccion = fields.Char("Direccion", size= 360)
    cpostal = fields.Integer("Código Postal", size= 5)
    
    venta_ids = fields.One2many('quintowood.venta', 'cliente_id', string='Ventas')

    @api.constrains('cpostal')
    def _check_cpostal(self):
        for record in self:
            if len(str(record.cpostal)) != 5 or not str(record.cpostal).isdigit():
                raise models.ValidationError("El código postal tiene que tener 5 dígitos")
            
    
    