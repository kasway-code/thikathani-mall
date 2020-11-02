from odoo import models, fields, api

class ProductTemplateAttributeValueWarehouse(models.Model):
    _inherit = 'product.template.attribute.value'
    
    warehouse_id = fields.Many2one(
        string='Almacen',
        comodel_name='stock.warehouse'
    )
     