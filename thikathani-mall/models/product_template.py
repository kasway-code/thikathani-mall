# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    descripcion_origen = fields.Text('Descripción y Origen')
    descripcion_beneficios = fields.Text('Beneficios')
    descripcion_usos = fields.Text('Modos de uso')
    
    brand_id = fields.Many2one('product.brand',string='Marca')
    type_id = fields.Many2one('product.type',string='Tipo')
    sku = fields.Char(string='SKU', compute='get_sku')

    @api.depends('sku')
    def get_sku(self):
        self.sku = str(self.brand_id) + "test"
    