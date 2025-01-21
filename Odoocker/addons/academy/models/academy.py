# -*- coding: utf-8 -*-
from odoo import models, fields, api
class academy(models.Model):
 _name = 'academy.academy'
 _descripcion = 'academy.academy'
 name= fields.Char('Class title', size=64, required=True)
 begin= fields.Datetime('Begin')
 end = fields.Datetime('End')
 capacity= fields.Integer('Capacity')
 contentType = fields.Selection([
 ('theorical','Theorical'),
 ('practical','Practical'),
 ('problems','Problems resolution'),
 ('intensive','Intensive')
 ],'Type of contents')