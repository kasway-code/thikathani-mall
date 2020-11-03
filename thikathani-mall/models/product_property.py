from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression

from odoo.tools import float_compare


class ProductProperty(models.Model):
    _name = "product.property"
    _description = "Product Property"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string='Name', index=True, required=True)
    complete_name = fields.Char(
        string='Complete Name', compute='_compute_complete_name', store=True)
    parent_id = fields.Many2one(
        string='Parent Property', comodel_name='product.property',  index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many(
        string='Child properties', comodel_name='product.property', inverse_name='parent_id')

    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image(
        "Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image(
        "Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image(
        "Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image(
        "Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    image_url = fields.Char(string='Imagen URL')
    odoo_image_url = fields.Char(
        string='Odoo Imagen URL', compute='_compute_odoo_image_url')

    @api.onchange('image_url')
    def _onchage_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.image_1920 = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.image_1920 = False

    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        for record in self:
            record.odoo_image_url = f'{web_base_url}/web/image/{self._name}/{record.id}/image_128'

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for proper in self:
            if proper.parent_id:
                proper.complete_name = '%s / %s' % (
                    proper.parent_id.complete_name, proper.name)
            else:
                proper.complete_name = proper.name

    @api.constrains('parent_id')
    def _check_property_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive properties.'))
        return True

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]
