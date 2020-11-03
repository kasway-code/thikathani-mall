import base64
import requests

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    internal_code = fields.Char(string='Código de la categoría')

    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)

    image_1024 = fields.Image(
        "Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image(
        "Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image(
        "Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image(
        "Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    image_url = fields.Char(string='Imagen URL')
    odoo_image_url = fields.Char(
        string='Odoo Imagen URL', compute='_compute_odoo_image_url')

    @api.onchange('image_url')
    def _onchage_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False

    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        for record in self:
            record.odoo_image_url = f'{web_base_url}/web/image/{self._name}/{record.id}/image_256'
