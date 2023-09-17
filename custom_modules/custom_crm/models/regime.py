from odoo import models, fields, api


class Regime(models.Model):
    _name = 'regime.regime'



    name = fields.Char(string ="Régime")