from odoo import models, fields, api
class Users(models.Model):
    _inherit = 'res.users'

    replace_id = fields.Many2one('res.users' , string="Replace")

    phone = fields.Char()