# -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_books(models.Model):
    _name = 'my_books.my_books'
    _description = 'my_books.my_books'
    name = fields.Char(string="Title", required=True)
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
