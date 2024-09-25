# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# class website_asaid_popup_extension(models.Model):
#     _name = 'website_asaid_popup_extension.website_asaid_popup_extension'
#     _description = 'website_asaid_popup_extension.website_asaid_popup_extension'


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields

class WebsitePopup(models.Model):
    _inherit = 'ir.ui.view'

    always_show = fields.Boolean(string='Always Show', default=False)
