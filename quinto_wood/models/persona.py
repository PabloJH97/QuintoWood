# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class Persona(models.Model):
    _name = 'quinto_wood.persona' # modulo.modelo
    _description = 'Una persona'

    name = fields.Char('Nombre', size=128, required = True)
    apellidos = fields.Char('Apellidos', size=128, required = True)
    dni = fields.Char("DNI",size=9, required= True)
    email = fields.Char("Email", size=70)
    movil = fields.Integer("Teléfono", size=9, required = True)

    _sql_constraints = [
        ('dni_uniq', 'UNIQUE(dni)', 'El DNI debe ser único'),
    ]
    
    
    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if len(record.dni) != 9 or not record.dni.isdigit():
                raise models.ValidationError("El DNI debe tener 9 dígitos")
            
   
    
    @api.constrains('name','apellidos')
    def _check_name(self):
        for record in self:
            if len(record.name) < 1 or len(record.apellidos) < 1:
                raise models.ValidationError("El nombre y los apellidos deben tener al menos 1 caracter")
            
    @api.constrains('email')  
    def _check_email(self):
        for record in self:
            if record.email and not '@' in record.email: #xra q valide el @ sólo si está lleno el campo
                raise models.ValidationError("El email debe tener un formato válido")