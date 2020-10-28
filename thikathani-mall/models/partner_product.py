from odoo import models, fields, api

class PartnerProductFavorite(models.Model):
    _name = 'partner.product.favorite'
    _description = 'Productos favoritos de un cliente'
    
    partner_id = fields.Many2one('res.partner', 'Cliente', required=True)
    product_id = fields.Many2one('product.template', 'Producto', required=True)

    is_favorite = fields.Boolean('Favorito')