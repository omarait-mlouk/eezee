# -*- coding: utf-8 -*-
# from odoo import http


# class EezeeBase(http.Controller):
#     @http.route('/eezee_base/eezee_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eezee_base/eezee_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eezee_base.listing', {
#             'root': '/eezee_base/eezee_base',
#             'objects': http.request.env['eezee_base.eezee_base'].search([]),
#         })

#     @http.route('/eezee_base/eezee_base/objects/<model("eezee_base.eezee_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eezee_base.object', {
#             'object': obj
#         })

