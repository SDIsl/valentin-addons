###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    show_hardware_properties = fields.Boolean(
        string='Hardware properties',
        help='Show hardware properties on item',
    )

    @api.onchange('show_hardware_properties')
    def _onchange_show_hardware_properties(self):
        if self.show_hardware_properties:
            self.env['product.template'].search([
                ('categ_id.id', '=', self._origin.id),
            ]).write({'internal_equipment': True})
        else:
            self.env['workspace.item'].search([
                ('product_id.categ_id.id', '=', self._origin.id),
            ]).write({
                'cpu': False,
                'ram': False,
                'data_storage': False,
                'ip': False,
                'os_version': False,
                'microsoft_office_mail': False
            })
