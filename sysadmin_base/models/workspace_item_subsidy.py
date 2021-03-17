###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class WorkspaceItemSubsidy(models.Model):
    _name = 'workspace.item.subsidy'
    _description = 'Subsidy'

    item_ids = fields.One2many(
        comodel_name='workspace.item',
        inverse_name='subsidy_id',
        string='Items',
    )
    name = fields.Char(
        string='Name',
    )
    description = fields.Char(
        string='Description',
    )
    date = fields.Date(
        string='Date',
    )
