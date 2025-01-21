# -*- coding: utf-8 -*-
from odoo import models, fields, api
class cuenta(models.Model):
    _name='banco.cuenta'
    _description='Una cuenta'
    numcuenta=fields.Integer("Id de cuenta", required=True)
    tipo=fields.Selection([('libreta', 'Libreta'), ('ahorro', 'Cuenta de ahorros'), ('corriente', 'Cuenta corriente'), ('deposito', 'Depósito')], 'Tipos de cuenta', default='libreta')
    saldo=fields.Float("Saldo de la cuenta", (10,2))
    state=fields.Selection([('activa', 'Activa'), ('inactiva', 'Inactiva'), ('baja', 'Baja')], 'Estado de la cuenta')