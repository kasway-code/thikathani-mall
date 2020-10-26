import base64
import requests

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'
    internal_code = fields.Char('Código de la categoría')

    image = fields.Binary(string='Image', compute='_compute_image')
    image_url = fields.Char(string='Imagen URL')

    
    @api.depends('image')
    def _compute_image(self):
        if not self.image_url:
            return 
        else:
            self.image = base64.b64encode(requests.get(self.image_url).content)
    #@api.onchange('image_url')
    #def _onchange_image_url(self):
    #    if not self.image_url:
    #        return 
    #    else:
    #        self.image = base64.b64encode(requests.get(self.image_url).content)
