import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression

from odoo.tools import float_compare

_logger = logging.getLogger(__name__)


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
        comodel_name='product.property.line',
        inverse_name='property_id',
    )

    image_url = fields.Char(string='Imagen URL')
    property_image = fields.Binary(string='Image')

    @api.onchange('image_url')
    def _onchange_image_url(self):
        if self.image_url != False and self.image_url != "":
            self.property_image = base64.b64encode(
                requests.get(self.image_url).content)
        else:
            self.property_image = False

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for property in self:
            if property.parent_id:
                property.complete_name = '%s / %s' % (
                    property.parent_id.complete_name, property.name)
            else:
                property.complete_name = property.name

    @api.constrains('parent_id')
    def _check_property_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive properties.'))
        return True

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]

    def unlink(self):
        main_property = self.env.ref('product.product_property_all')
        if main_property in self:
            raise UserError(
                _("You cannot delete this product property, it is the default generic property."))
        return super().unlink()


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
