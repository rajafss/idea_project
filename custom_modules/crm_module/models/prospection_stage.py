from odoo import models, fields, api
class ProspectionStage(models.Model):
    _name='prospection.stage'


    name = fields.Char(string="Prospection stage")
