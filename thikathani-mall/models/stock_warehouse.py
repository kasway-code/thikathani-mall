# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'
    # Supported
    city = fields.One2many('res.partner', 'partner_id', related="partner_id.city", readonly=True)

    # state =
    # district =
    # image_url =
