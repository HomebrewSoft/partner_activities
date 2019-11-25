# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    p_activity_ids = fields.Many2many(
        comodel_name='res.partner.activity',
        string=_('Activity'),
    )
