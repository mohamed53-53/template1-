# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError
from dateutil import relativedelta

from datetime import date


class HrContract(models.Model):
    _inherit = "hr.contract"

    allowance_id = fields.One2many('allowance.type', "salary_info_id", string="Allowance Types")
    value_type = fields.Selection([('fixed', 'Fixed'), ('percentage', 'Percentage')], string='Value Type')
    value = fields.Float(string="Value")
    increase_type = fields.Selection([('per_day', 'Per day'), ('full', 'Full')], string='Increase Type')
    structure_type_id = fields.Many2one('hr.payroll.structure.type', string='Salary Structure Type')
    salary_type = fields.Many2many("hr.salary.rule", string='Salary Type',domain="[('struct_id.type_id.name','=','Employee')]")



    @api.onchange("structure_type_id")
    def onchange_structure_type(self):
        if self.structure_type_id:
            return {'domain': {'salary_type': [('struct_id.type_id', '=', self.structure_type_id.id)]}}
