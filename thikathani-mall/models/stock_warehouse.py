# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'
    # Supported
    # 'partner_city': fields.related('res.partne', 'city', readonly=True, type='char', store=True)
    #city = fields.One2many('res.partner', 'partner_id', related="partner_id.city", readonly=True)

    city = fields.Char('City', related='partner_id.city', readonly=True)
    country = fields.Char(related='partner_id.state_id.country_id.name', string="Country")
    #state = fields.Many2one(
    #    'State', related='partner_id.state_id', readonly=True, store=True)
    #country = fields.Many2one('Country', related='partner_id.country_id', readonly=True, store=True)
    # district = fields.Char('District', related='partner_id.l10n_pe_district', readonly=True)
    # image_url =
