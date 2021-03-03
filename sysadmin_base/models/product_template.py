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
    item_count = fields.Integer(
        'Items',
        compute='_compute_item_count',
    )

    @api.one
    def _compute_item_count(self):
        self.item_count = self.env['workspace.item'].search(
            [('product_id', '=', self.id)],
            count=True,
        )

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
            'context': {'default_product_id': self.id},
            'domain': [('product_id', '=', self.id)]
        }
