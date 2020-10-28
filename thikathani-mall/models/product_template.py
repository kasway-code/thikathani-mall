import base64
import requests

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descripcion_origen = fields.Text('Descripción y Origen')
    descripcion_beneficios = fields.Text('Beneficios')
    descripcion_usos = fields.Text('Modos de uso')
    
    brand_id = fields.Many2one('product.brand',string='Marca')
    sku = fields.Char(string='SKU', compute='get_sku')

    #property_ids = fields.One2many(
    #    string='Propiedades',
    #    comodel_name='product.property',
    #    inverse_name='id',
    #)
    

    image_url = fields.Char(string='Imagen URL')
    image_1920 = fields.Binary(string='Image')

    @api.depends('sku')
    def get_sku(self):
        self.sku = str(self.brand_id) + "test"
        
    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(requests.get(self.image_url).content)
        else:
            self.image_1920 = False
    