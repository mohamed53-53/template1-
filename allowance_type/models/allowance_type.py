# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError
from dateutil import relativedelta

from datetime import date


class AllowanceType(models.Model):
    _name = "allowance.type"
    _description = "Allowance Type"

    gas_allowance = fields.Integer(string='Gas Allowance', translate=True)
    tips_allowance = fields.Integer(string='Tips Allowance', translate=True)
    bonus_allowance = fields.Integer(string='Bonus Allowance', translate=True)
    salary_info_id = fields.Many2one("hr.contract")
