# -*- coding: utf-8 -*-
from odoo import models, fields, api
'''
class ProductBrand(models.Model):
    _name = 'product.brand'
    code = fields.Char('Codigo')
    brand_name = fields.Char('Nombre')
'''

class BrandProduct(models.Model):
    _name = 'product.brand'

    name= fields.Char("Nombre")
    brand_image = fields.Binary()
    products_ids = fields.One2many('product.template', 'brand_id')
   
    product_count = fields.Char("Cantidad", compute='get_count_products', store=True)

    @api.depends('products_ids')
    def get_count_products(self):
        self.product_count = len(self.products_ids)

class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id  = fields.Many2one(related='product_id.brand_id', string='Brand', store=True, readonly=True)