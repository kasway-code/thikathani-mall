import base64
import requests

from odoo import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'
    #logo = fields.Binary(related='partner_id.image_1920', default=_get_logo, string="Company Logo", readonly=False)
    #logo_url = fields.Char('Logo URL')
    #    compute='_compute_logo_url')
    
    #@api.depends('depends')
    #def _compute_logo_url(self):
    #    for record in self:
     #       record.logo_url=something
    
    #@api.onchange('logo_url')
    #def _onchange_logo_url(self):
    #    if not self.logo_url:
    #        return 
    #    else:
    #        self.logo = base64.b64encode(requests.get(self.logo_url).content)