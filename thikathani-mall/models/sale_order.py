import base64
import requests

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    numero_guia = fields.Char(string='Numero de guia')
    product_tmpl_list = fields.One2many(
        string='Lista de productos', comodel_name='sale.order.line', inverse_name='order_id', compute='_compute_product_tmpl_list', store=True)

    # product_tmpl_list = fields.Char(
    #    string='Lista de productos', compute='_compute_product_tmpl_list'
    # )

    @api.onchange('numero_guia')
    def _compute_product_tmpl_list(self):
        for record in self:
            record.product_tmpl_list = self.env['sale.order.line'].search_read([('order_id', '=', record.id)])
            '''
            record.product_tmpl_list = [
                {
                    "id": 8,
                    "name": "AGUA ALCALINA 250ML ALKA+",
                    "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.template/8/image_1920",
                    "price": 0.0,
                    "property_list": [
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
                },
                {
                    "id": 13,
                    "name": "Desk Organizer",
                    "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.template/13/image_1920",
                    "price": 0.0,
                    "property_list": [
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
                },
                {
                    "id": 2,
                    "name": "Discount",
                    "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.template/2/image_1920",
                    "price": 0.0,
                    "property_list": [
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
                }
            ]
            '''
