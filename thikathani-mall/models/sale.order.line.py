import base64
import requests
import json

from odoo import models, fields, api


class OrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    '''
    product_tmpl_property_ids =  fields.One2many(
        string='Field Name',
        comodel_name='model.name',
        inverse_name='inverse_field',
    )
    '''
    