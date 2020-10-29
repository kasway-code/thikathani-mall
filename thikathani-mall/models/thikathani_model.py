import base64
import requests

from odoo import models, fields, api

class ThikaThani(models.Model):
    odoo_image_url = fields.Char(string='Odoo Imagen URL', compute='_compute_odoo_image_url' )