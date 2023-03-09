from odoo import fields, models, api
from ast import literal_eval


class ConfSetting(models.TransientModel):
    _inherit = "res.config.settings"

    discount_limit = fields.Monetary(string="Discount Limit", related='pos_config_id.discount', store=True, readonly=False)
    category_ids = fields.Many2many('pos.category', 'category_rel',
                                    'rel_pos_dis', 'rel_cat')

    def set_values(self):
        res = super(ConfSetting, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'pos_session_wise_discount.category_ids', self.category_ids.ids)
        return res

    @api.model
    def get_values(self):
        res = super(ConfSetting, self).get_values()
        with_user = self.env['ir.config_parameter'].sudo()
        com_contacts = with_user.get_param(
            'pos_session_wise_discount.category_ids')
        res.update(category_ids=[(6, 0, literal_eval(com_contacts))
                                 ] if com_contacts else False, )
        return res


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount = fields.Monetary()

    @api.model
    def get_categories(self):
        categories = self.env['ir.config_parameter'].sudo().get_param(
            'pos_session_wise_discount.category_ids')
        categories_list = eval(categories)
        # print(categories_list)
        # print(type(categories_list))
        return categories_list
