from odoo import models, fields, api
from datetime import date

class GearMaintenanceRequest(models.Model):
    _name = "gear.maintenance.request"
    _description = "Maintenance Request"

    name = fields.Char(string="Subject", required=True)

    equipment_id = fields.Many2one(
        "gear.equipment",
        string="Equipment",
        required=True
    )

    team_id = fields.Many2one(
        "gear.maintenance.team",
        string="Maintenance Team"
    )

    technician_id = fields.Many2one(
        "res.users",
        string="Assigned Technician"
    )

    request_type = fields.Selection(
        [
            ("corrective", "Corrective"),
            ("preventive", "Preventive"),
        ],
        string="Request Type",
        required=True,
        default="corrective"
    )

    scheduled_date = fields.Date(string="Scheduled Date")
    duration = fields.Float(string="Hours Spent")

    state = fields.Selection(
        [
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("repaired", "Repaired"),
            ("scrap", "Scrap"),
        ],
        default="new"
    )

    is_overdue = fields.Boolean(
        string="Overdue",
        compute="_compute_overdue"
    )

    @api.onchange("equipment_id")
    def _onchange_equipment(self):
        if self.equipment_id:
            self.team_id = self.equipment_id.maintenance_team_id

    @api.depends("scheduled_date", "state")
    def _compute_overdue(self):
        today = date.today()
        for rec in self:
            rec.is_overdue = (
                rec.scheduled_date
                and rec.scheduled_date < today
                and rec.state not in ["repaired", "scrap"]
            )
        
    def action_mark_scrap(self):
        for rec in self:
            rec.state = "scrap"
            rec.equipment_id.is_scrapped = True
