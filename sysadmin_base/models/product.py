###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class Product(models.Model):
    _inherit = 'product'

    internat_equipment = fields.Boolean(string='Internal equipment')

    # first_type
    # subtype

    s_n = fields.Char(string='S/N')
    ip = fields.Char(string='IP')
    ios_version = fields.Char(string='IOS Version')
    ram = fields.Char(string='RAM')
    cpu = fields.Char(string='CPU')
    data_storage = fields.Char(string='Data storage')
