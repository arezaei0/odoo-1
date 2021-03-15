# -*- coding: utf-8 -*-
# from odoo import http


# class C:\odoo\odoo\custom-addons\libraryApp(http.Controller):
#     @http.route('/c:\odoo\odoo\custom-addons\library_app/c:\odoo\odoo\custom-addons\library_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\odoo\odoo\custom-addons\library_app/c:\odoo\odoo\custom-addons\library_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\odoo\odoo\custom-addons\library_app.listing', {
#             'root': '/c:\odoo\odoo\custom-addons\library_app/c:\odoo\odoo\custom-addons\library_app',
#             'objects': http.request.env['c:\odoo\odoo\custom-addons\library_app.c:\odoo\odoo\custom-addons\library_app'].search([]),
#         })

#     @http.route('/c:\odoo\odoo\custom-addons\library_app/c:\odoo\odoo\custom-addons\library_app/objects/<model("c:\odoo\odoo\custom-addons\library_app.c:\odoo\odoo\custom-addons\library_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\odoo\odoo\custom-addons\library_app.object', {
#             'object': obj
#         })
