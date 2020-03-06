# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo.addons.component.core import Component
from odoo import _


class PingService(Component):
    _inherit = "base.rest.service"
    _name = "emc.services"
    _usage = "ping"  # service_name
    _collection = "emc.services"
    _description = """

    """

    def ping(self):
        return {"message": _("This is a ping from Easy My Coop API")}

    def search(self):
        return {"message": _("This is a ping from Easy My Coop API")}

    def _validator_ping(self):
        return {}

    def _validator_return_ping(self):
        return {"message": {"type": "string"}}

    def _validator_search(self):
        return {}

    def _validator_return_search(self):
        return {"message": {"type": "string"}}