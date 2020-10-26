# -*- coding: utf-8 -*-
from odoo import http

'''
class ProductIlo(http.Controller):
    @http.route('/product_ilo/product_ilo/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/product_ilo/product_ilo/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('product_ilo.listing', {
            'root': '/product_ilo/product_ilo',
            'objects': http.request.env['product_ilo.product_ilo'].search([]),
        })

    @http.route('/product_ilo/product_ilo/objects/<model("product_ilo.product_ilo"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('product_ilo.object', {
            'object': obj
        })
'''

class ProductTemplate(http.Controller):
    @http.route('/efact/efact/',type="json" , auth='public')
    def index(self, **kw):
        return {"msg":"Hello, world"}