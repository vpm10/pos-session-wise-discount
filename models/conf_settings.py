from odoo import fields, models


class ConfSetting(models.TransientModel):
    _inherit = "res.config.settings"

    discount_limit = fields.Monetary(string="Discount Limit", store=True)
    category_ids = fields.Many2many('pos.category', 'category_rel', 'rel_pos_dis', 'rel_cat')
