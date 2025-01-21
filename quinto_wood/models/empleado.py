# -*- coding: utf-8 -*-

from odoo import models, fields, api


class empleado(models.Model):
    _name = 'persona.empleado' # modulo.modelo
    _inherit = 'quintowood.persona' # hay q hacerlo por prototipo
    _description = 'Un empleado'

    
    salario = fields.Float("Salario", size=5, default=0)
    puesto= fields.Char("Puesto", size=128)
    fotodni = fields.Binary("Foto")

    venta_ids = fields.One2many('quintowood.venta', 'empleado_id', string='Ventas')
    
    
    @api.constrains('salario')
    def _check_salario(self):
        for record in self:
            if record.salario <= 0:
                raise models.ValidationError('El salario no puede ser nagativo ni 0.')

_sql_constraints = [
    ('puesto_not_null', 'CHECK(puesto IS NOT NULL)', 'El campo puesto no puede ser nulo.')
]