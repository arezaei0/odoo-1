# -*- coding: utf-8 -*-
# from odoo import http


# class –help(http.Controller):
#     @http.route('/–help/–help/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/–help/–help/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('–help.listing', {
#             'root': '/–help/–help',
#             'objects': http.request.env['–help.–help'].search([]),
#         })

#     @http.route('/–help/–help/objects/<model("–help.–help"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('–help.object', {
#             'object': obj
#         })
