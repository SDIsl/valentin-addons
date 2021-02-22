###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    internal_equipment = fields.Boolean(
        string='Internal equipment',
    )
    information = fields.Text(
        string='Information',
    )
    hardware_properties = fields.Boolean(
        readonly=True,
        store=True,
        related='categ_id.show_hardware_properties',
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
    item_count = fields.Integer(
        compute='_compute_item_count',
    )

    @api.one
    def _compute_item_count(self):
        self.item_count = len(self.env['workspace.item'].search([
            ('product_id', '=', self.id),
        ]))

    @api.onchange('categ_id')
    def _onchange_categ_id(self):
        if self.hardware_properties:
            self.internal_equipment = True

    def product_item_count(self):
        return{
            'name': 'Items',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'workspace.item',
            'type': 'ir.actions.act_window',
            'domain': [('product_id', '=', self.id)]
        }
