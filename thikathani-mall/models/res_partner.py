from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    country_name = fields.Char('Country', related='country_id.name', readonly=True)
    state_name = fields.Char('State', related='state_id.name', readonly=True)
    district_name = fields.Char('District', related='l10n_pe_district.name', readonly=True)
    
    odoo_image_url = fields.Char(string='Odoo Imagen URL', compute='_compute_odoo_image_url' )
    '''
    favorite_product_ids = fields.One2many(
        string='Favorite Product',
        comodel_name='partner.product.favorite',
        inverse_name='product_id',
    )
'''

    @api.depends('warehouse_image')
    def _compute_odoo_image_url(self):
        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.odoo_image_url = record.odoo_image_url = f'{web_base_url}/web/image/stock.warehouse/{record.id}/warehouse_image'