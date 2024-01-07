from odoo import models, fields, api
class Users(models.Model):
    _inherit = 'res.users'


    #we add this field to set the data for another user when  a current user in leave
    replace_id = fields.Many2one('res.users' , string="Replace")

    phone = fields.Char()