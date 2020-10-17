from odoo import models, fields, api

class ProductType(models.Model):
    _name = 'product.type'
    _description = 'Tipo de producto'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(string='Nombre', required=True)
    type_image = fields.Binary()