import base64
import requests

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descripcion_origen = fields.Text(string='Descripción y Origen')
    descripcion_beneficios = fields.Text(string='Beneficios')
    descripcion_usos = fields.Text(string='Modos de uso')
    # step_ids = fields.One2many(related='template_id.step_ids', string = "Steps") 

    brand_id = fields.Many2one(string='Marca',comodel = 'product.brand')
    brand_name = fields.Char(string='Nombre de la marca', related='brand_id.name', readonly=True)
 
    sku = fields.Char(string='SKU', compute='_compute_sku')

    property_line_ids = fields.One2many(
        string='Property Line',
        comodel_name='product.template.property.line',
        inverse_name='product_tmpl_id',
    )
    
    image_url = fields.Char(string='Imagen URL')
    image_1920 = fields.Binary(string='Image')
    odoo_image_url = fields.Char(string='Odoo Imagen URL', compute='_compute_odoo_image_url' )

    @api.depends('sku')
    def _compute_sku(self):
        for record in self:
            record['sku'] = f'{record.categ_id}-{record.brand_id}-record.product_id.x_consumption_rate'

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False
    
    @api.depends('image_1920')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/product.template/{record.id}/image_1920'
