import base64
import requests

from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    country_name = fields.Char('Country', related='partner_id.state_id.country_id.name', readonly=True)
    state_name = fields.Char('State', related='partner_id.state_id.name', readonly=True)
    city_name = fields.Char('City', related='partner_id.city_id.name', readonly=True)
    district_name = fields.Char('City', related='partner_id.l10n_pe_district.name', readonly=True)
    street_name = fields.Char('Street', related='partner_id.street', readonly=True)

    latitude = fields.Float('Latitud', related='partner_id.partner_latitude', readonly=True)
    longitude = fields.Float('Longitud', related='partner_id.partner_longitude', readonly=True)

    zip_code = fields.Char('Zip', related='partner_id.zip', readonly=True)

    warehouse_image = fields.Binary(string='Image')
    image_url = fields.Char(string='Imagen URL')
    odoo_image_url = fields.Char(string='Odoo Imagen URL', compute='_compute_odoo_image_url' )
    
    @api.onchange('image_url')
    def _onchage_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.warehouse_image = base64.b64encode(requests.get(self.image_url).content)
        else:
            self.warehouse_image = False
    
    @api.depends('warehouse_image')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/stock.warehouse/{record.id}/warehouse_image'
