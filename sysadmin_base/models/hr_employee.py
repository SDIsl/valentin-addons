###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    has_dialoga_access = fields.Boolean(
        string='Has Dialoga access',
    )
    is_trainee = fields.Boolean(
        string='Is trainee',
    )
    workspace_ids = fields.Many2many(
       'workspace.workspace',
       'employee_workspace_rel',
       'employee_id',
       'workspace_id',
       string='Workspaces',
    )
    item_ids = fields.One2many(
        'workspace.item',
        'employee_id',
        string='Items',
    )
