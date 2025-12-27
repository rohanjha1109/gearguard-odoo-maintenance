from odoo import models, fields

class GearEquipment(models.Model):
    _name = "gear.equipment"
    _description = "Company Equipment"

    name = fields.Char(string="Equipment Name", required=True)
    serial_number = fields.Char(string="Serial Number")

    purchase_date = fields.Date(string="Purchase Date")
    warranty_expiry = fields.Date(string="Warranty Expiry")

    location = fields.Char(string="Location")

    department = fields.Char(string="Department")
    employee_name = fields.Char(string="Assigned To")

    maintenance_team_id = fields.Many2one(
        "gear.maintenance.team",
        string="Maintenance Team",
        required=True
    )

    is_scrapped = fields.Boolean(string="Scrapped", default=False)

    request_count = fields.Integer(
        string="Maintenance Requests",
        compute="_compute_request_count"
    )

    def _compute_request_count(self):
        for rec in self:
            rec.request_count = self.env["gear.maintenance.request"].search_count([
                ("equipment_id", "=", rec.id),
                ("state", "!=", "repaired")
            ])

    def action_view_maintenance_requests(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Maintenance Requests",
            "res_model": "gear.maintenance.request",
            "view_mode": "tree,form,kanban",
            "domain": [("equipment_id", "=", self.id)],
        }
