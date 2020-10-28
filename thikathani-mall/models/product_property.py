from odoo import models, fields, api

class ProductProperty(models.Model):
    _name = 'product.property'
    #_inherit = 'product.category'
    
    # Cambiar a ProductProperty
    #name = fields.Char('Nombre', required=True)
    #property_image = fields.Binary()
    #products_ids = fields.One2many('product.template', 'type_id')