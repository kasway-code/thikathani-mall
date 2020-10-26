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

    
    es_organico = fields.Boolean(string='Organico')
    es_vegano = fields.Boolean(string='Vegano')
    es_vegetariano = fields.Boolean(string='Vegetariano')
    es_keto = fields.Boolean(string='Keto')
    es_usda = fields.Boolean(string='USDA')
    es_sin_gluten = fields.Boolean(string='Sin gluten')
    es_sin_lactosa = fields.Boolean(string='Sin lactosa')
    es_sin_azucar = fields.Boolean(string='Sin azucar')
    es_non_gmo = fields.Boolean(string='NON GMO')
    
    image_url = fields.Char(string='Imagen URL')
    image_1920 = fields.Binary(string='Image', compute='_compute_image')

    @api.depends('sku')
    def get_sku(self):
        self.sku = str(self.brand_id) + "test"

    @api.depends('image_1920')
    def _compute_image(self):
        if self.image_url != False:
            self.image_1920 = base64.b64encode(requests.get(self.image_url).content)
        else:
            self.image_1920 = self.image_1920
    