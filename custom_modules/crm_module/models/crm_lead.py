
from odoo import models, fields, api
class CrmLead(models.Model):
    _inherit = 'crm.lead'

    ################################################
    #Fields
    ################################################
    replace_id = fields.Many2one('res.users' , string="Replace", related="user_id.replace_id")

    product = fields.Many2one(
        'product.template',
        string="Product/Service")

    argument_ids = fields.Many2many("argument.argument" ,string="Argument" , related="product.argument_ids")

    prospection_stage_id = fields.Many2many('prospection.stage',  related="product.prospection_stage_id")

    description = fields.Text(related="product.description")

    partner_id = fields.Many2one(
        'res.partner', string='Prospect', check_company=True, index=True, tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.")
    is_draft = fields.Boolean(related="stage_id.is_draft")
    #  compute fields
    email_p = fields.Char(
        'Email', tracking=40, index='trigram',
        compute='_compute_email_from', readonly=False, store=True)

    phone = fields.Char(
        'Phone', tracking=50,
        compute='_compute_phone', readonly=False, store=True)


    # we need a function compute to genrate email and phone of partner
    def _compute_email_from(self):
        """To get the default email of contacts,,, we get just the email factory"""
        for lead in self:
            lead.email_p = lead.partner_id.email_factory

    def _compute_phone(self):
        """To get the default phone of contacts,,, we get just the phone factory"""
        for lead in self:
            lead.phone = lead.partner_id.phone_factory







class CustomCRMStage(models.Model):
    _inherit = 'crm.stage'

    # Add your custom fields here, e.g., a draft stage
    is_draft = fields.Boolean()