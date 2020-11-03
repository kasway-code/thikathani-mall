import base64
import requests

from odoo import models, fields, api


class BrandProduct(models.Model):
    _name = 'product.brand'
    name = fields.Char(string="Nombre de la marca")
    internal_code = fields.Char('Código de la marca')

    product_tmpl_ids = fields.One2many(string='Productos',
                                       comodel_name='product.template', inverse_name='brand_id')
    product_count = fields.Char(
        string="Cantidad", compute='get_count_members', store=True)

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

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for proper in self:
            if proper.parent_id:
                proper.complete_name = '%s / %s' % (
                    proper.parent_id.complete_name, proper.name)
            else:
                proper.complete_name = proper.name

    @api.depends('product_tmpl_ids')
    def get_count_members(self):
        self.product_count = len(self.product_tmpl_ids)


class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id = fields.Many2one(
        related='product_id.brand_id', string='Brand', store=True, readonly=True)
