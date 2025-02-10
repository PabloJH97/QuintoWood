# -*- coding: utf-8 -*-

from odoo import models, fields, api


class empleado(models.Model):
    _name = 'quinto_wood.empleado' # modulo.modelo
    _inherit = 'quinto_wood.persona' # hay q hacerlo por prototipo
    _description = 'Un empleado'

    
    salario = fields.Float("Salario", size=5, default=0)
    puesto= fields.Char("Puesto", size=128)
    fotodni = fields.Binary("Foto")

    venta_ids = fields.One2many('quinto_wood.venta', 'empleado_id', string='Ventas')
    
    
    @api.constrains('salario')
    def _check_salario(self):
        for record in self:
            if record.salario <= 0:
                raise models.ValidationError('El salario no puede ser nagativo ni 0.')

_sql_constraints = [
    ('puesto_not_null', 'CHECK(puesto IS NOT NULL)', 'El campo puesto no puede ser nulo.')
]

@api.model
def write(self, vals):
        if 'salario' in vals:
            for record in self:
                nuevo_salario = vals.get('salario', record.salario)
                if nuevo_salario < 1000:
                    raise models.ValidationError("El salario no puede ser menor a 1000 debido al SMI")
        return super(empleado, self).write(vals)
    
    
@api.model
def actualizar_salarios_10(self):
    empleados = self.search([('salario', '<', 1000)])
    for empleado in empleados:
        empleado.salario += 100
        
@api.model
def actualizar_salarios_20(self):
    empleados = self.search([('salario', '<', 1000)])
    for empleado in empleados:
        empleado.salario += 200
        
def aplicar_bonus(self):
    empleados = self.env['quinto_wood.empleado'].search([('puesto', '=', "Jefe de zona")])
    for empleado in empleados:
        empleado.salario += 500  