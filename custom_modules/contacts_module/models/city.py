from odoo import models, fields


class City(models.Model):
    _name = 'delegation'
    _rec_name = 'city'


    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
