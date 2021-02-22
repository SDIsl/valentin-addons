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


    def employee_item_count(self):
        return{
            'name': 'Items',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'workspace.item',
            'type': 'ir.actions.act_window',
            'domain': [('workspace_id', 'in', self.workspace_ids.ids)]
        }
