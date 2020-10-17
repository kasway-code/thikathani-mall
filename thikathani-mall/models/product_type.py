from odoo import models, fields, api

class ProductType(models.Model):
    _name = 'product.type'
    _description = 'Tipo de producto'
    name = fields.Char(string='Nombre', required=True)
    type_image = fields.Binary()
    products_ids = fields.One2many('product.template', 'type_id')