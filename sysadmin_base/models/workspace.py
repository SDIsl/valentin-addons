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
        string='Description',
    )
    location = fields.Char(
        string='Location',
    )
    item_count = fields.Integer(
        'Items',
        compute='_compute_item_count',
    )
    employee_count = fields.Integer(
        'Employee Count',
        compute='_compute_employee_count',
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
        self.item_count = self.env['workspace.item'].search(
            [('workspace_id', '=', self.id)],
            count=True,
        )

    @api.one
    def _compute_employee_count(self):
        self.employee_count = self.env['hr.employee'].search(
            [('workspace_ids', 'like', self.id)],
            count=True,
        )

    def workspace_item_count(self):
        return{
            'name': 'Items',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'workspace.item',
            'type': 'ir.actions.act_window',
            'context': {'default_workspace_id': self.id},
            'domain': [('workspace_id', '=', self.id)],
        }


class WorkspaceItem(models.Model):
    _name = 'workspace.item'
    _description = 'Item'

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    sn = fields.Char(
        string='Serial Number',
        copy=False,
    )
    _sql_constraints = [
        ('sn_unique', 'unique(sn)', 'SN already exists!')
    ]
    subsidy_id = fields.Many2one(
        'workspace.item.subsidy',
        'Subsidy',
    )
    hardware_properties = fields.Boolean(
        readonly=True,
        store=True,
        related='product_id.categ_id.show_hardware_properties',
    )
    cpu = fields.Char(
        string='CPU',
    )
    ram = fields.Selection([
        ('RAM2GB', '2 GB'),
        ('RAM4GB', '4 GB'),
        ('RAM6GB', '6 GB'),
        ('RAM8GB', '8 GB'),
        ('RAM10GB', '10 GB'),
        ('RAM12GB', '12 GB'),
        ('RAM16GB', '16 GB'),
        ('RAM20GB', '20 GB'),
        ('RAM24GB', '24 GB'),
        ('RAM32GB', '32 GB'),
        ('RAM48GB', '48 GB'),
        ('RAM64GB', '64 GB'),
        ('RAM96GB', '96 GB'),
        ('RAM128GB', '128 GB'),
    ], 'RAM')
    data_storage = fields.Char(
        string='Data storage',
    )
    ip = fields.Char(
        string='IP',
    )
    os_version = fields.Char(
        string='OS Version',
    )
    microsoft_office_mail = fields.Char(
        string='Microsoft Office Mail',
    )
    product_id = fields.Many2one(
        'product.template',
        'Product',
        required=True,
        domain=[('internal_equipment', '=', 'True')],
    )
    workspace_id = fields.Many2one(
        'workspace.workspace',
        'Workspace',
        group_expand='_expand_workspace_ids',
    )
    workspace_location = fields.Char(
        string='Workspace location',
        readonly=True,
        store=True,
        related='workspace_id.location',
    )
    employee_id = fields.Many2one(
        'hr.employee',
        'Employee',
    )

    @api.model
    def _expand_workspace_ids(self, workspaces, domain, order):
        return self.env['workspace.workspace'].search([
            ('employee_ids.user_id', '=', self.env.uid)
        ])

    @api.onchange('workspace_id')
    def _check_workspace(self):
        if self.workspace_id:
            self.employee_id = False

    @api.onchange('employee_id')
    def _check_employee(self):
        if self.employee_id:
            self.workspace_id = False

    class WorkspaceItemSubsidy(models.Model):
        _name = 'workspace.item.subsidy'
        _description = 'Subsidy'

        name = fields.Char(
            string='Name'
        )
        description = fields.Char(
            string='Description',
        )
        date = fields.Date(
            string='Date',
        )
        item_ids = fields.One2many(
            'workspace.item',
            'subsidy_id',
            string='Items'
        )
