from odoo import models, fields, api

class ProductType(models.Model):
    _name = 'product.type'
    name = fields.Char('Nombre', required=True)
    type_image = fields.Binary()
    products_ids = fields.One2many('product.template', 'type_id')