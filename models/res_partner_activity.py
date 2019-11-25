# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PartnerActivity(models.Model):
    _name = 'res.partner.activity'
    _description = 'Partner activity'

    name = fields.Char(
    )
