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

    name = fields.Char('Name', index=True, required=True)
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True)
    parent_id = fields.Many2one(
        'product.property', 'Parent Property', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many(
        'product.property', 'parent_id', 'Child properties')

    property_line_ids = fields.One2many(
        string='Property Line',
        comodel_name='product.template.property.line',
        inverse_name='property_id',
    )

    property_image = fields.Binary(string='Image')
    image_url = fields.Char(string='Imagen URL')
    odoo_image_url = fields.Char(
        string='Odoo Imagen URL', compute='_compute_odoo_image_url', store=True)

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.property_image = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.property_image = False

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

    @api.depends('property_image')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        for record in self:
            record.odoo_image_url = f'{web_base_url}/web/image/product.property/{record.id}/property_image'

'''
class ProductPropertyLine(models.Model):
    _name = "product.template.property.line"
    product_tmpl_id = fields.Many2one(
        string='Producto',
        comodel_name='product.template'
    )

    property_id = fields.Many2one(
        string='Propiedad',
        comodel_name='product.property'
    )

    property_name = fields.Char(
        'Nombre de la propiedad', related='property_id.name', readonly=True)
    property_image = fields.Binary(
        'Imagen de la propiedad', related='property_id.property_image', readonly=True)
    odoo_image_url = fields.Char(
        'URL de la imagen', related='property_id.odoo_image_url', readonly=True)
'''