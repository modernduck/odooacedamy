# -*- coding: utf-8 -*-
from openerp import http

# class Newlife(http.Controller):
#     @http.route('/newlife/newlife/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/newlife/newlife/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('newlife.listing', {
#             'root': '/newlife/newlife',
#             'objects': http.request.env['newlife.newlife'].search([]),
#         })

#     @http.route('/newlife/newlife/objects/<model("newlife.newlife"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('newlife.object', {
#             'object': obj
#         })