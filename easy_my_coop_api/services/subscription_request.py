# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.addons.component.core import Component


class SubscriptionRequestService(Component):
    _inherit = "base.rest.service"
    _name = "subscription.request.services"
    _usage = "subscription_request"  # service_name
    _collection = "emc.services"
    _description = """

    """
