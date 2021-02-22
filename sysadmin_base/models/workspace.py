###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class Workspace(models.Model):
    _name = 'workspace.workspace'
    _description = 'Workspace'

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Char(
        string="Description",
    )
    location = fields.Char(
        string='Location',
    )
    item_count = fields.Integer(
        'Items',
        compute='_compute_item_count',
    )
    employee_ids = fields.Many2many(
        'hr.employee',
        'employee_workspace_rel',
        'workspace_id',
        'employee_id',
        string='Employees',
    )

    @api.one
    def _compute_item_count(self):
        self.item_count = len(self.env['workspace.item'].search([
            ('workspace_id', '=', self.id),
        ]))

    def workspace_item_count(self):
        return{
            'name': 'Items',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'workspace.item',
            'type': 'ir.actions.act_window',
            'domain': [('workspace_id', '=', self.id)]
        }


class WorkspaceItem(models.Model):
    _name = 'workspace.item'
    _description = 'Item'

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string="Description",
    )
    sn = fields.Char(
        string="Serial Number",
    )
    product_id = fields.Many2one(
        'product.template',
        'Product',
        required=True,
    )
    workspace_id = fields.Many2one(
        'workspace.workspace',
        'Workspace',
        required=True,
        group_expand='_expand_workspace_ids'
    )

    @api.model
    def _expand_workspace_ids(self, workspaces, domain, order):
        return self.env['workspace.workspace'].search([
            ('employee_ids.user_id', '=', self.env.uid)
        ])
