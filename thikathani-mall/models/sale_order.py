import base64
import requests

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    numero_guia = fields.Char(string='Numero de guia')
    product_tmpl_list = fields.One2many(
        string='Lista de productos', comodel_name='product.template', inverse_name='product_tmpl_id', compute='_compute_product_tmpl_list')

    @api.onchange('numero_guia')
    def _compute_product_tmpl_list(self):
        for record in self:
            record.product_tmpl_list = [
                {
                    "id": 1,
                    "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.property/1/property_image"
                },
                {
                    "id": 2,
                    "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.property/2/property_image"
                },
                {
                    "id": 3,
                    "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.property/3/property_image"
                }
            ]
