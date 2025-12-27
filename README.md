# GearGuard – Odoo Maintenance Tracker

GearGuard is a custom Odoo-style maintenance management module built for the **Odoo Hackathon – Virtual Round**.  
The module focuses on tracking company equipment and managing corrective and preventive maintenance requests by connecting equipment, maintenance teams, and workflows.

---

## Module Overview

The module is designed around three core entities:

- **Equipment** – Company assets such as machines, vehicles, or IT devices
- **Maintenance Teams** – Specialized teams responsible for maintaining equipment
- **Maintenance Requests** – Corrective (breakdown) and preventive (scheduled) maintenance tasks

The goal is to provide a structured maintenance workflow similar to Odoo’s native maintenance concepts.

---

## Key Features

- Equipment management with ownership and maintenance team assignment  
- Maintenance team management with assigned technicians  
- Corrective and preventive maintenance requests  
- Automatic maintenance team auto-fill when equipment is selected  
- Workflow states: New, In Progress, Repaired, Scrap  
- Kanban view for maintenance execution workflow  
- Calendar view for preventive maintenance scheduling  
- Smart button on equipment to view related maintenance requests  
- Scrap logic to mark equipment as unusable when scrapped  

---

## Workflow Summary

1. A user creates a maintenance request and selects equipment  
2. The maintenance team is automatically filled based on the equipment record  
3. Requests move through workflow states using the Kanban view  
4. Preventive maintenance requests appear in a calendar based on scheduled date  
5. If a request is scrapped, the related equipment is marked as unusable  

---

## Reference Mockup

The following mockup was **provided as part of the hackathon problem statement** and was used only as a reference to align the workflow and user interface design:

https://link.excalidraw.com/l/65VNwvy7c4X/5y5Qt87q1Qp

---

## Technical Approach

- Implemented using **standard Odoo module architecture**
- Business logic written using **Odoo ORM concepts**
- User interface defined using **Odoo XML views**
- Focused on clarity, workflow correctness, and alignment with problem requirements

---

## Tech Stack

- Odoo (Community Edition concepts)
- Python (Odoo ORM)
- XML (Odoo Views)

---

## Notes

This project was developed as part of the **virtual evaluation round**.  
The implementation focuses on correct module structure, workflow logic, and design alignment rather than deployment or production configuration.