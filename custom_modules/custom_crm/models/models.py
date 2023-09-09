from odoo import models, fields


class CustomCRMLead(models.Model):
    _inherit = 'crm.lead'


    # prospect = fields.Many2one('res.partner', string="Contacts")
    # product = fields





