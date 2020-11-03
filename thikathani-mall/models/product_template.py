import base64
import requests

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    description_origin = fields.Text(string='Descripción y Origen')
    description_benefits = fields.Text(string='Beneficios')
    description_uses = fields.Text(string='Modos de uso')

    brand_id = fields.Many2one(string='Marca', comodel_name='product.brand')
    brand_name = fields.Char(string='Nombre de la marca',
                             related='brand_id.name', readonly=True)

    sku = fields.Char(string='SKU', compute='_compute_sku', store=True)

    property_line_ids = fields.Many2many(
        string='Property Id',
        comodel_name='product.property',
        relation='product_property_product_template_rel',
        column1='product_property_id',
        column2='product_template_id',
    )

    product_property_list = fields.Char(
        string='Lista de propiedades', compute='_compute_property_list')

    image_url = fields.Char(string='Imagen URL')
    odoo_image_url = fields.Char(
        string='Odoo Imagen URL', compute='_compute_odoo_image_url', store=True)

    @api.depends('categ_id', 'brand_id')
    def _compute_sku(self):
        for record in self:
            categ_code = record.categ_id.internal_code
            subcateg_code = record.categ_id.parent_id.internal_code
            brand_code = record.brand_id.internal_code
            record['sku'] = f'{categ_code}-{subcateg_code}-{brand_code}-'

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False

    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/product.template/{record.id}/image_256'

    @api.depends('property_line_ids')
    def _compute_property_list(self):
        for record in self:
            product_property_list = self.env['product.property'].read_group([record.property_line_ids], ['name','odoo_image_url'])
            record.product_property_list = str(json.dumps(product_property_list))