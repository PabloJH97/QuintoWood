# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class Cliente(models.Model):
    _name = 'quinto_wood.cliente' # modulo.modelo
    _inherit= 'quinto_wood.persona'
    _description = 'Un cliente'

    direccion = fields.Char("Direccion", size= 360)
    cpostal = fields.Integer("Código Postal", size= 5)
    
    venta_ids = fields.One2many('quinto_wood.venta', 'cliente_id', string='Ventas')

    @api.constrains('cpostal')
    def _check_cpostal(self):
        for record in self:
            if len(record.cpostal) != 5 or not (record.cpostal).isdigit():
                raise models.ValidationError("El código postal tiene que tener 5 dígitos.")
      
    @api.model
    def clientes_con_ventas(self):
        return self.env['quinto_wood.cliente'].search([('venta_ids', '!=', False)])
    
  
    @api.constrains('cpostal')
    def unlink(self):
        for record in self:
            if record.venta_ids:
             raise models.ValidationError("No se puede eliminar un cliente que tiene alguna venta.")
        return super(Cliente, self).unlink()
    
    def actualizar_direccion(self):
        clientes = self.env['quinto_wood.cliente'].search([('cpostal', '=', '41089')])
        clientes.write({'direccion': 'Montequinto, Sevilla'})
        
        