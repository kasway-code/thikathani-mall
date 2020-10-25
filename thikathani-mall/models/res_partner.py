# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'
    # Supported
    #'partner_city': fields.related('res.partne', 'city', readonly=True, type='char', store=True)
    #city = fields.One2many('res.partner', 'partner_id', related="partner_id.city", readonly=True)
