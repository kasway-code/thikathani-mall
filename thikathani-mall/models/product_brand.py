# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BrandProduct(models.Model):
    _name = 'product.brand'

    name= fields.Char("Nombre")
    extras= fields.Char("Extras")
    
    members_ids = fields.One2many('product.template', 'brand_id')
    product_count = fields.Char("Cantidad", compute='get_count_members', store=True)

    brand_image = fields.Binary()
    image_url = fields.Char(string='Imagen URL')

    @api.onchange('image_url')
    def _onchage_image_url(self):
        if not self.image_url:
            self.image = base64.b64encode(requests.get(self.image_url).content)
        else:
            self.image = False

    @api.depends('members_ids')
    def get_count_members(self):
        self.product_count = len(self.members_ids)

class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id  = fields.Many2one(related='product_id.brand_id', string='Brand', store=True, readonly=True)