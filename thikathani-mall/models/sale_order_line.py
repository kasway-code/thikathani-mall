import base64
import requests
import json

from odoo import models, fields, api


class OrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    #Campo existente
    # product_template_id = fields.Many2one(
    #    string='Producto',
    #    comodel_name='product.template'
    #)

    product_tmpl_property_ids =  fields.Many2many(
        string='Propiedades de productos',
        comodel_name='product.property'
    )
    
    @api.depends()
    def _compute_property_list():
        for rec in record:
            product_tmpl_property_ids = self.env['product.template.property.line'].search_read([('product_tmpl_id', '=', rec['product_template_id'].id)], ['odoo_image_url'])
            record['product_tmpl_property_ids'] = str(json.dumps(product_tmpl_property_ids))