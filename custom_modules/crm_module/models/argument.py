from odoo import models, fields, api

class Argument(models.Model):
    _name= 'argument.argument'



    question_text = fields.Text(string="Question")
    response_text = fields.Text(string="Response")

