###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class Workspace(models.Model):
    _name = 'workspace.workspace'
    _description = 'Workspace'

    item_ids = fields.One2many(
        comodel_name='workspace.item',
        inverse_name='workspace_id',
        string='Items',
    )
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        relation='employee_workspace_rel',
        column1='workspace_id',
        column2='employee_id',
        string='Employees',
    )
    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Char(
        string='Description',
    )
    location = fields.Char(
        string='Location',
    )
    employee_count = fields.Integer(
        string='Employee Count',
        compute='_compute_employee_count',
    )

    @api.one
    def _compute_employee_count(self):
        self.employee_count = self.env['hr.employee'].search(
            [('workspace_ids', 'like', self.id)],
            count=True,
        )
