from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    country_name = fields.Char('Country', related='country_id.name', readonly=True)
    state_name = fields.Char('State', related='state_id.name', readonly=True)
    district_name = fields.Char('District', related='l10n_pe_district.name', readonly=True)