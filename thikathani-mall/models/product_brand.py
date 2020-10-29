import base64
import requests

from odoo import models, fields, api


class BrandProduct(models.Model):
    _name = 'product.brand'
    name = fields.Char(string="Nombre de la marca")

    product_tmpl_ids = fields.One2many(string='Productos',
                                       comodel_name='product.template', inverse_name='brand_id')
    product_count = fields.Char(
        string="Cantidad", compute='get_count_members', store=True)

    brand_image = fields.Binary(string='Image')
    image_url = fields.Char(string='Imagen URL')

    @api.onchange('image_url')
    def _onchage_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.brand_image = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.brand_image = False

    @api.depends('product_tmpl_ids')
    def get_count_members(self):
        self.product_count = len(self.product_tmpl_ids)

    @api.depends('brand_image')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/product.brand/{record.id}/brand_image'


class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id = fields.Many2one(
        related='product_id.brand_id', string='Brand', store=True, readonly=True)
