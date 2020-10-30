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
        if self._model_name == "product.template":
            for rec in record:
                property_list = models.execute_kw(
                    self._db, uid, self._pass, 'product.template.property.line', 'read', [rec['product_template_id'].id], {'fields': ['odoo_image_url']})
                rec['product_tmpl_property_ids'] = property_list