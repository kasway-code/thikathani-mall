# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = 'product.category'
    internal_code = fields.Char('Código de la categoría')