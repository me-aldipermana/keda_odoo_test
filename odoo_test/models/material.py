# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'material'
    _description = ' Material'

    _sql_constraints = [('code_material_unique', 'unique(code)', 'Code must be unique !')]

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], required=True)
    buy_price = fields.Float(required=True)
    partner_id = fields.Many2one('res.partner', ondelete='restrict', required=True)

    @api.constrains('buy_price')
    def _check_value(self):
        if self.buy_price > 100 or self.buy_price < 1:
            raise ValidationError(_('Enter Buy Price Value Between 1-100.'))
