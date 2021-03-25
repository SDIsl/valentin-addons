###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class WorkspaceItem(models.Model):
    _name = 'workspace.item'
    _description = 'Item'
    _sql_constraints = [
        (
            'sn_unique',
            'unique(sn)',
            'SN already exists!',
        ),
    ]

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    amount = fields.Integer(
        string='Amount',
        default=1,
        help='It can\'t be lower than 0.',
    )
    sn = fields.Char(
        string='Serial Number',
        copy=False,
    )
    subsidy_id = fields.Many2one(
        comodel_name='workspace.item.subsidy',
        string='Subsidy',
    )
    hardware_properties = fields.Boolean(
        readonly=True,
        store=True,
        related='product_id.categ_id.show_hardware_properties',
    )
    cpu = fields.Char(
        string='CPU',
    )
    ram = fields.Selection(
        selection=[
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
        ],
        string='RAM',
    )
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
        comodel_name='product.template',
        string='Product',
        required=True,
        domain=[('internal_equipment', '=', 'True')],
    )
    workspace_id = fields.Many2one(
        comodel_name='workspace.workspace',
        string='Workspace',
        group_expand='_expand_workspace_ids',
    )
    workspace_location = fields.Char(
        string='Workspace location',
        readonly=True,
        store=True,
        related='workspace_id.location',
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
    )
    employee_location = fields.Char(
        string='Employee location',
        readonly=True,
        store=True,
        related='employee_id.work_location',
    )

    @api.model
    def _expand_workspace_ids(self, workspaces, domain, order):
        return self.env['workspace.workspace'].search([
            ('employee_ids.user_id', '=', self.env.uid)
        ])

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.name = self.product_id.name

    @api.onchange('workspace_id')
    def _check_workspace(self):
        if self.workspace_id:
            self.employee_id = False

    @api.onchange('employee_id')
    def _check_employee(self):
        if self.employee_id:
            self.workspace_id = False

    @api.onchange('amount')
    def _onchange_amount(self):
        if self.amount > 1:
            self.sn = False

    @api.onchange('sn')
    def _onchange_sn(self):
        if self.sn:
            self.amount = 1
