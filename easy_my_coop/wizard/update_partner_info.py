# -*- coding: utf-8 -*-

from openerp import api, fields, models


class PartnerUpdateInfo(models.TransientModel):
    _name = "partner.update.info"
    _description = "Update Partner Info"

    @api.model
    def _get_partner(self):
        active_id = self.env.context.get('active_id')
        return self.env['res.partner'].browse(active_id)

    @api.model
    def _get_register_number(self):
        partner = self._get_partner()
        if partner.is_company:
            return partner.company_register_number

    register_number = fields.Char(string="Register Number",
                                  default=_get_register_number)
    cooperator = fields.Many2one('res.partner',
                                 string="Cooperator",
                                 default=_get_partner)
    all = fields.Boolean(string="Update from subscription request")
    birthdate = fields.Boolean(string="set missing birth date")

    @api.multi
    def update(self):
        partner_obj = self.env['res.partner']
        cooperator = self.cooperator
        coop_vals = {}

        if self.all:
            if self.birthdate:
                coops = partner_obj.search([('cooperator', '=', True),
                                            ('birthdate_date', '=', False),
                                            ('is_company', '=', False)])
                for coop in coops:
                    if coop.subscription_request_ids:
                        sub_req = coop.subscription_request_ids[0]
                        coop.birthdate_date = sub_req.birthdate
        else:
            if cooperator:
                if cooperator.is_company:
                    coop_vals['company_register_number'] = self.register_number
                if coop_vals:
                    cooperator.write(coop_vals)

        return True
