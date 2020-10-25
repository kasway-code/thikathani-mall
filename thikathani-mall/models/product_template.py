# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    logo_url = fields.Char('Logo URL')

    descripcion_origen = fields.Text('Descripción y Origen')
    descripcion_beneficios = fields.Text('Beneficios')
    descripcion_usos = fields.Text('Modos de uso')
    
    brand_id = fields.Many2one('product.brand',string='Marca')
    type_id = fields.Many2one('product.type',string='Tipo')
    sku = fields.Char(string='SKU', compute='get_sku')

    
    es_organico = fields.Boolean(string='Organico')
    es_vegano = fields.Boolean(string='Vegano')
    es_vegetariano = fields.Boolean(string='Vegetariano')
    es_keto = fields.Boolean(string='Keto')
    es_usda = fields.Boolean(string='USDA')
    es_sin_gluten = fields.Boolean(string='Sin gluten')
    es_sin_lactosa = fields.Boolean(string='Sin lactosa')
    es_sin_azucar = fields.Boolean(string='Sin azucar')
    es_non_gmo = fields.Boolean(string='NON GMO')

    @api.depends('sku')
    def get_sku(self):
        self.sku = str(self.brand_id) + "test"

    @api.onchange('logo_url')
    def _onchange_logo_url(self):
        if not self.logo_url:
            return 
        else:
            self.logo = base64.b64encode(requests.get(self.logo_url).content)
    