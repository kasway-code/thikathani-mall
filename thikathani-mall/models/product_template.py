import base64
import requests

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descripcion_origen = fields.Text('Descripción y Origen')
    descripcion_beneficios = fields.Text('Beneficios')
    descripcion_usos = fields.Text('Modos de uso')
    # step_ids = fields.One2many(related='template_id.step_ids', string = "Steps") 
    brand_id = fields.Many2one('product.brand', string='Marca')
    brand_name = fields.Char('Nombre de la marca', related='brand_id.name', readonly=True)
    type_id = fields.Many2one('product.type', string='Tipo')
    sku = fields.Char(string='SKU', compute='get_sku')

    property_line_ids = fields.One2many(
        string='Property Line',
        comodel_name='product.template.property.line',
        inverse_name='product_tmpl_id',
    )
    
    image_url = fields.Char(string='Imagen URL')
    image_1920 = fields.Binary(string='Image')
    odoo_image_url = fields.Char(string='Odoo Imagen URL', compute='_compute_odoo_image_url' )
    
    @api.depends('sku')
    def get_sku(self):
        self.sku = str(self.brand_id) + "test"

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False
    
    @api.depends('warehouse_image')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/stock.warehouse/{record.id}/warehouse_image'
