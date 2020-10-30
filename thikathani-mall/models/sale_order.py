import base64
import requests
import json

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    numero_guia = fields.Char(string='Numero de guia')

    #product_tmpl_list = fields.One2many(
    #    string='Lista de productos', comodel_name='sale.order.line', inverse_name='order_id', compute='_compute_product_tmpl_list', store=True)

    product_tmpl_list = fields.Char(
        string='Lista de productos', compute='_compute_product_tmpl_list')

    @api.onchange('numero_guia')
    def _compute_product_tmpl_list(self):
        for record in self:
            product_tmpl_list = self.env['sale.order.line'].search_read([('order_id', '=', record.id)], ['name','price_unit', 'discount','product_tmpl_property_ids'])
            record.product_tmpl_list = str(json.dumps(product_tmpl_list))