# -*- coding: utf-8 -*-

from odoo import models, fields, api


class book(models.Model):
    _name = 'library.book' # modulo.modelo
    _description = 'Un libro'

    title = fields.Char('Titulo',size=128)
    image = fields.Binary("Imagen")
    isbn = fields.Char("ISBN",size=16)
    npage = fields.Integer("Nº de páginas", default=100)
    type  = fields.Selection([('fantasia', 'Novela fantástica'),
                              ('historia', 'Ensayo histórico')], "Género", default='historia') 