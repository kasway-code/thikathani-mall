from odoo import models, fields, api

class ProductProperty(models.Model):
    _name = 'product.property'
    name = fields.Char("Name")