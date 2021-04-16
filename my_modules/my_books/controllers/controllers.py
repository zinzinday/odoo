# -*- coding: utf-8 -*-
from odoo import http


class MyBooks(http.Controller):

    @http.route('/my_books/my_books/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_books/my_books/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('my_books.listing', {
            'root': '/my_books/my_books',
            'objects': http.request.env['my_books.my_books'].search([]),
        })

    @http.route('/my_books/my_books/objects/<model("my_books.my_books"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_books.object', {
            'object': obj
        })
