from odoo import models, fields


class Legal(models.Model):
    _name = 'forme.juridique'


    name = fields.Char(string="legal status")