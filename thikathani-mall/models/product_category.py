import base64
import requests

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'
    internal_code = fields.Char('Código de la categoría')

    image = fields.Binary(string='Image')
    image_url = fields.Char(string='Imagen URL')

    
    @api.onchange('image_url')
    def _onchage_image(self):
        if self.image_url != False:
            self.image = base64.b64encode(requests.get(self.image_url).content)
    #@api.onchange('image_url')
    #def _onchange_image_url(self):
    #    if not self.image_url:
    #        return 
    #    else:
    #        self.image = base64.b64encode(requests.get(self.image_url).content)
