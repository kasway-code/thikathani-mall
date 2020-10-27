from odoo import models, fields, api

class TypeProduct(models.Model):
    _name = 'product.type'
    
    # Cambiar a ProductProperty
    name = fields.Char('Nombre', required=True)
    type_image = fields.Binary()
    products_ids = fields.One2many('product.template', 'type_id')