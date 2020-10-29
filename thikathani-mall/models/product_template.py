import base64
import requests

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descripcion_origen = fields.Text(string='Descripción y Origen')
    descripcion_beneficios = fields.Text(string='Beneficios')
    descripcion_usos = fields.Text(string='Modos de uso')
    # step_ids = fields.One2many(related='template_id.step_ids', string = "Steps")

    brand_id = fields.Many2one(string='Marca', comodel_name='product.brand')
    brand_name = fields.Char(string='Nombre de la marca',
                             related='brand_id.name', readonly=True)

    sku = fields.Char(string='SKU', compute='_compute_sku')

    property_line_ids = fields.One2many(
        string='Propiedades',
        comodel_name='product.template.property.line',
        inverse_name='product_tmpl_id',
    )

    property_list = fields.One2many(string='Property List', comodel_name='product.template.property.line', inverse_name='product_tmpl_id', compute= '_compute_sku')
    #property_list = fields.One2many(string='Property List')
    image_url = fields.Char(string='Imagen URL')
    image_1920 = fields.Binary(string='Image')
    odoo_image_url = fields.Char(
        string='Odoo Imagen URL', compute='_compute_odoo_image_url')

    @api.onchange('brand_id')
    def _compute_sku(self):
        for record in self:
            record['sku'] = f'{record.categ_id.internal_code}-{record.brand_id.internal_code}-record.product_id.x_consumption_rate'
            #record.property_list = self.env["product.template.property.line"]
            #record.property_list = record.property_line_ids.read(['property_image'])
            record.property_list = [
            {
                "id": 1,
                "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.property/1/property_image"
            },
            {
                "id": 2,
                "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.property/2/property_image"
            },
            {
                "id": 3,
                "odoo_image_url": "https://kasway-code-thikathani-mall-mall-1581943.dev.odoo.com/web/image/product.property/3/property_image"
            }
        ]

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False

    @api.depends('image_1920')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/product.template/{record.id}/image_1920'

    @api.depends()
    def _compute_property_list():
        if self._model_name == "product.template":
            for rec in record:
                property_list = models.execute_kw(
                    self._db, uid, self._pass, 'product.property', 'read', [rec['property_line_ids']], {'fields': ['odoo_image_url']})
                rec['property_list'] = property_list
