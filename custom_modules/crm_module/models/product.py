from odoo import models, fields, api




class ProductproductArgument(models.Model):
    _inherit = 'product.product'


    argument_ids = fields.Many2many("argument.argument" ,string="Argument")

class ProductArgument(models.Model):
    _inherit = 'product.template'


    argument_ids = fields.Many2many("argument.argument" ,string="Argument")

    description = fields.Text()



# class ProductproductArgument(models.Model):
#     _inherit = 'crm.lead'




