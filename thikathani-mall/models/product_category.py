import base64
import requests

from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = ['product.category', 'image.mixin']
    internal_code = fields.Char('Código de la categoría')

    #category_image = fields.Binary(string='Image')
    image_url = fields.Char(string='Imagen URL')
    odoo_image_url = fields.Char(string='Odoo Imagen URL', compute='_compute_odoo_image_url' )

    @api.onchange('image_url')
    def _onchage_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(requests.get(self.image_url).content)
        else:
            self.image_1920 = False
            
    @api.depends('image_1920')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/product.category/{record.id}/image_1920'