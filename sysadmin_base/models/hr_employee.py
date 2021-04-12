###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    has_voip_switchboard_access = fields.Boolean(
        string='Has VoIP Switchboard access',
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
        readonly=True,
    )
    item_ids = fields.One2many(
        comodel_name='workspace.item',
        inverse_name='employee_id',
        string='Items',
    )
    item_count = fields.Integer(
        string="Item Count",
        compute="_compute_item_count",
    )

    @api.one
    def _compute_item_count(self):
        self.item_count = 0
        for item in self.item_ids:
            self.item_count += item.amount

    def button_employee_items(self):
        return{
            'name': 'Employee\'s Items',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'workspace.item',
            'type': 'ir.actions.act_window',
            'domain': [('employee_id', '=', self.id)],
        }

    def action_button_internal_tools(self):
        self.ensure_one()
        view = self.env.ref(
            'sysadmin_base.employee_internal_tools_view_form')
        return {
            'name': 'Edit Internal Tools',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hr.employee.internal_tools',
            'view_id': view.id,
            'views': [(view.id, 'form')],
            'context': {
                'default_employee_id': self.id,
                'default_has_voip_switchboard_access': self.has_voip_switchboard_access,
                'default_is_trainee': self.is_trainee,
            },
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
