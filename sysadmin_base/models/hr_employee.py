###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    has_dialoga_access = fields.Boolean(
        string='Has Dialoga access',
    )
    is_trainee = fields.Boolean(
        string='Is trainee',
    )
    workspace_ids = fields.Many2many(
        comodel_name='workspace.workspace',
        relation='employee_workspace_rel',
        column1='employee_id',
        column2='workspace_id',
        string='Workspaces',
    )
    item_ids = fields.One2many(
        comodel_name='workspace.item',
        inverse_name='employee_id',
        string='Items',
    )

    def button_employee_items(self):
        return{
            'name': 'My Items',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'workspace.item',
            'type': 'ir.actions.act_window',
            'domain': [('employee_id', '=', self.id)],
        }
