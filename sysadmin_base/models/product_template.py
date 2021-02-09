###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


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
    ram = fields.Char(
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
