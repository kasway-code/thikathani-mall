import base64
import requests

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descripcion_origen = fields.Text('Descripción y Origen')
    descripcion_beneficios = fields.Text('Beneficios')
    descripcion_usos = fields.Text('Modos de uso')
    # step_ids = fields.One2many(related='template_id.step_ids', string = "Steps") 
    brand_id = fields.Many2one('product.brand', string='Marca')
    type_id = fields.Many2one('product.type', string='Tipo')
    sku = fields.Char(string='SKU', compute='get_sku')

    property_ids = fields.One2many(
        string='Propiedades',
        comodel_name='product.property'
    )

   #property_images = fields.One2many(
    #    string='Iconos de propiedades',
   #     comodel_name='product.property',
   #     inverse_name='property_image',
   # )

    image_url = fields.Char(string='Imagen URL')
    image_1920 = fields.Binary(string='Image')

    @api.depends('sku')
    def get_sku(self):
        self.sku = str(self.brand_id) + "test"

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False
