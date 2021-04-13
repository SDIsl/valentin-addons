###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class HrEmployeeInternalTools(models.TransientModel):
    _name = 'hr.employee.internal_tools'
    _description = 'Assistant to edit internal tools of employees'

    employee_id = fields.Integer(
        string='Employee ID',
    )
    name = fields.Char(
        string='Name',
    )
    has_voip_switchboard_access = fields.Boolean(
        string='Has VoIP Switchboard access',
    )
    is_trainee = fields.Boolean(
        string='Is trainee',
    )
    workspace_ids = fields.Many2many(
        comodel_name='workspace.workspace',
        string='Workspaces',
    )
    item_ids = fields.Many2many(
        comodel_name='workspace.item',
        string='Items',
    )

    def edit_employee_internal_tools_action(self):
        self.ensure_one()
        self.sudo().env['hr.employee'].search([
            ('id', '=', self.employee_id),
        ]).write({
            'has_voip_switchboard_access': self.has_voip_switchboard_access,
            'is_trainee': self.is_trainee,
            'item_ids': [(6, 0, self.item_ids.ids)],
            'workspace_ids': [(6, 0, self.workspace_ids.ids)],
        })
