import base64
import requests

from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'
    # Supported
    # 'partner_city': fields.related('res.partne', 'city', readonly=True, type='char', store=True)
    #city = fields.One2many('res.partner', 'partner_id', related="partner_id.city", readonly=True)

    
    country = fields.Char('Country', related='partner_id.state_id.country_id.name', readonly=True)
    state = fields.Char('State', related='partner_id.state_id.name', readonly=True)
    city = fields.Char('City', related='partner_id.city_id.name', readonly=True)
    district = fields.Char('City', related='partner_id.l10n_pe_district.name', readonly=True)
    street = fields.Char('Street', related='partner_id.street', readonly=True)

    latitude = fields.Float('Latitud', related='partner_id.partner_latitude', readonly=True)
    longitude = fields.Float('Longitud', related='partner_id.partner_longitude', readonly=True)

    zip_code = fields.Char('Zip', related='partner_id.zip', readonly=True)

    image = fields.Binary(string='Image')
    image_url = fields.Char(string='Imagen URL')

    
    @api.onchange('image_url')
    def _onchage_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image = base64.b64encode(requests.get(self.image_url).content)
        else:
            self.image = False


    #state = fields.Many2one(
    #    'State', related='partner_id.state_id', readonly=True, store=True)
    #country = fields.Many2one('Country', related='partner_id.country_id', readonly=True, store=True)
    # district = fields.Char('District', related='partner_id.l10n_pe_district', readonly=True)
    # image_url =
