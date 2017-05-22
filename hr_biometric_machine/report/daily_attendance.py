
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import tools, _
from odoo import models, fields, api

class report_daily_attendance(models.Model):
    _name = 'report.daily.attendance'
    _auto = False
    

    name = fields.Many2one('hr.employee','Employee')
    day = fields.Date('Date')
    address_id = fields.Many2one('res.partner', 'Working Address')
    category = fields.Char('category')
    punch = fields.Integer('Number of Punch')
    in_punch = fields.Datetime('In Punch')
    out_punch = fields.Datetime('Out Punch')

    _order = 'day desc'
    def init(self):
        tools.drop_view_if_exists(self._cr, 'report_daily_attendance')
        self._cr.execute("""
            create or replace view report_daily_attendance as (
                select 
                    min(h.id) as id,
                    h.employee_id as name, 
                    Count(h.check_out) as punch,
                    h.write_date as day,
                    e.address_id as address_id,
                    e.category as category,
                    min(h.check_in) as in_punch ,
                    case when min(h.check_in) != max(h.check_in) then max(h.check_in)  end as out_punch   
                from hr_attendance h
                    join hr_employee e on (h.employee_id=e.id)

                GROUP BY 
                    h.employee_id,
                    h.write_date,
                    e.address_id,
                    e.category
            
            )
        """)
