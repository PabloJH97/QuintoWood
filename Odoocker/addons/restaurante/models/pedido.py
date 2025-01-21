# -*- coding: utf-8 -*-
from odoo import models, fields, api
class pedido(models.Model):
    _name='restaurante.pedido'
    _description='Un pedido'
    ordernumber=fields.Integer("Número de pedido", required=True)
    table=fields.Integer("Número de mesa", required=True)
    waiter=fields.Char("Nombre del camarero", size=50, required=True)
    orderTime=fields.Datetime("Hora de creación del pedido", required=True)
    price=fields.Float("Precio", required=True)
    productname=fields.Char("Nombre del producto", required=True)
    state=fields.Selection([("registrado", "Registrado"), ("preparandose", "Preparándose"), ("listo", "Listo"), ("servido", "Servido")], "Estado del pedido" ,required=True)
