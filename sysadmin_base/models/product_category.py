###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    show_hardware_properties = fields.Boolean(
        string='Hardware properties',
        help='Show hardware properties on product')
