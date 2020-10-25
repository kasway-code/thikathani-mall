# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'
    # Supported
    #'partner_city': fields.related('res.partne', 'city', readonly=True, type='char', store=True)
    #city = fields.One2many('res.partner', 'partner_id', related="partner_id.city", readonly=True)

    partner_city = fields.Char('City', related='partner_id.city', readonly=True)
    #partner_state = fields.Char('State', related='partner_id.state', readonly=True)
    # state =
    # district =
    # image_url =
