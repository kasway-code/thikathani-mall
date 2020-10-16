# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductBrand(models.Model):
    _name = 'product.brand'
    code = fields.Char('Codigo')
    name = fields.Char('Nombre')
