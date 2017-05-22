# -*- coding: utf-8 -*-

import logging
import time

from odoo import models, fields, api
from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from zklib import zklib
from zklib import zkconst


<<<<<<< HEAD
# inherit hr_employee module
=======
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
class hr_employee(models.Model):
    _inherit = 'hr.employee'

    emp_code = fields.Char("Emp Code")
    category = fields.Char("Category")
<<<<<<< HEAD


# inherit hr_attendance module
=======
    
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
class hr_attendance(models.Model):
    _inherit = 'hr.attendance'

    emp_code = fields.Char("Emp Code")
<<<<<<< HEAD

    # overriding the __check_validity fucntion to not check the "check_out" value for employee attendance
=======
    
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_validity(self):
        """ Verifies the validity of the attendance record compared to the others from the same employee.
            For the same employee we must have :
                * maximum 1 "open" attendance record (without check_out)
                * no overlapping time slices with previous employee records
        """
        for attendance in self:
            # we take the latest attendance before our check_in time and check it doesn't overlap with ours
            last_attendance_before_check_in = self.env['hr.attendance'].search([
                ('employee_id', '=', attendance.employee_id.id),
                ('check_in', '<=', attendance.check_in),
                ('id', '!=', attendance.id),
<<<<<<< HEAD
             ], order='check_in desc', limit=1)
=======
            ], order='check_in desc', limit=1)
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
            if last_attendance_before_check_in and last_attendance_before_check_in.check_out and last_attendance_before_check_in.check_out >= attendance.check_in:
                raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee was already checked in on %(datetime)s") % {
                    'empl_name': attendance.employee_id.name_related,
                    'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(attendance.check_in))),
<<<<<<< HEAD
                 })

            # Commented out the attendance.checkout checking
=======
                })

>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
            if not attendance.check_out:
                # if our attendance is "open" (no check_out), we verify there is no other "open" attendance
                no_check_out_attendances = self.env['hr.attendance'].search([
                    ('employee_id', '=', attendance.employee_id.id),
                    ('check_out', '=', False),
                    ('id', '!=', attendance.id),
<<<<<<< HEAD
                 ])
                if no_check_out_attendances:
                    pass
                    # raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee hasn't checked out since %(datetime)s") % {
                    #    'empl_name': attendance.employee_id.name_related,
                    #    'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(no_check_out_attendances.check_in))),
                    # })
=======
                ])
                if no_check_out_attendances:
                    pass
                   # raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee hasn't checked out since %(datetime)s") % {
                    #    'empl_name': attendance.employee_id.name_related,
                    #    'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(no_check_out_attendances.check_in))),
                    #})
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
            else:
                # we verify that the latest attendance with check_in time before our check_out time
                # is the same as the one before our check_in time computed before, otherwise it overlaps
                last_attendance_before_check_out = self.env['hr.attendance'].search([
                    ('employee_id', '=', attendance.employee_id.id),
                    ('check_in', '<=', attendance.check_out),
                    ('id', '!=', attendance.id),
<<<<<<< HEAD
                 ], order='check_in desc', limit=1)
=======
                ], order='check_in desc', limit=1)
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
                if last_attendance_before_check_out and last_attendance_before_check_in != last_attendance_before_check_out:
                    raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee was already checked in on %(datetime)s") % {
                        'empl_name': attendance.employee_id.name_related,
                        'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(last_attendance_before_check_out.check_in))),
<<<<<<< HEAD
                     })


# biometric machine module
class biometric_machine(models.Model):
    _name = 'biometric.machine'

=======
                    })



class biometric_machine(models.Model):
    _name= 'biometric.machine'
    
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
    name = fields.Char("Machine IP")
    ref_name = fields.Char("Location")
    port = fields.Integer("Port Number")
    address_id = fields.Many2one('res.partner', string='Partner')
<<<<<<< HEAD
    company_id = fields.Many2one("res.company", string='Company Name')

    # function to download attendance
    @api.multi
    def download_attendance(self):
=======
    company_id = fields.Many2one("res.company",string='Company Name')




    def download_attendance(self):
        hr_employee = self.env['hr.employee'].browse()  
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
        hr_attendance = self.env['hr.attendance'].browse()
        for info in self:
            machine_ip = info.name
            port = info.port
<<<<<<< HEAD

            # connect to the biometric device using the machine ip and port
            zk = zklib.ZKLib(machine_ip, int(port))
            res = zk.connect()
            if res:
                zk.enableDevice()
                user = zk.getUser()
                attendance = zk.getAttendance()
                if (attendance):
                    # get the user data from the biometric device
                    user = zk.getUser()
                    for lattendance in attendance:
                        time_att = str(lattendance[2].date()) + ' ' + str(lattendance[2].time())
                        atten_time = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                        atten_time = datetime.strftime(atten_time, '%Y-%m-%d %I:%M:%S')
                        in_time = datetime.strptime(atten_time, '%Y-%m-%d %H:%M:%S').time()
                        time_new = str(in_time)
                        time_new = time_new.replace(":", ".", 1)
                        time_new = time_new[0:5]
                        check_in = fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(atten_time))),
                        if user:
                            for uid in user:
                                # compare the employee code in user data with employee code in attendance data of each employee in the attendance list
                                # only matched users are processed
                                if user[uid][0] == str(lattendance[0]):
                                    get_user_id = self.env['hr.employee'].search([('emp_code', '=', str(lattendance[0]))])
                                    if get_user_id:

                                        # check for duplicate attendance values
                                        duplicate_atten_ids = self.env['hr.attendance'].search([('emp_code', '=', str(lattendance[0])), ('check_in', '=', check_in)])
                                        if duplicate_atten_ids:
                                            continue
                                        else:
                                            # create attendance values to hr.attendance table
                                            search_user_id = self.env['hr.employee'].search([('name', '=', user[uid][1]), ('emp_code', '=', str(lattendance[0]))])
                                            if search_user_id:
                                                data = hr_attendance.create({'employee_id': get_user_id.id, 'emp_code': lattendance[0], 'check_in': check_in})
                                    else:
                                        employee = self.env['hr.employee'].create({'emp_code': str(lattendance[0]), 'name': user[uid][1]})
                                        data = hr_attendance.create({'employee_id': employee.id, 'emp_code': lattendance[0], 'check_in': check_in})
                                else:
                                    pass

                    zk.enableDevice()
                    zk.disconnect()
                    return True
                else:
                    raise ValidationError(_('Warning !'), _("Unable to get the attendance log, please try again later."))
            else:
                raise ValidationError(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))

    # Dowload attendence data regularly
    @api.multi
    def schedule_download(self, ids=None):

=======
            
            #connect to the biometric device using the machine ip and port
            zk = zklib.ZKLib(machine_ip, int(port))
            res = zk.connect()
            if res == True:
                
                #ping the biometric device
                zk.enableDevice()
                zk.disableDevice()
                zk.enableDevice()
                zk.disableDevice() 
                
                # get the attendance from the biometric machine
                attendance = zk.getAttendance()
                
                #ping the biometric device
                zk.enableDevice()
                zk.disableDevice()
                zk.enableDevice()
                zk.disableDevice() 
                
       
                if attendance:
                    
                    #get the user data from the biometric device
                    data_user = zk.getUser() 
                    for lattendance in attendance:
                        time_att = str(lattendance[2].date()) + ' ' +str(lattendance[2].time())
                        atten_time = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                        atten_time = datetime.strftime(atten_time,'%Y-%m-%d %H:%M:%S')
                        in_time = datetime.strptime(atten_time,'%Y-%m-%d %H:%M:%S').time()

                        time_new = str(in_time)
                        time_new = time_new.replace(":",".",1)
                        time_new = time_new[0:5]
                        if data_user:       
                            for uid in data_user: 
                                #compare the employee code in user data with employee code in attendance data of each employee in the attendance list
                                #only matched users are processed
                                if data_user[uid][0] == str(lattendance[0]):
                                    get_user_id = self.env['hr.employee'].search([('emp_code', '=', str(lattendance[0]))]) 
                                    if get_user_id:
                                        
                                        #check for duplicate attendance values
                                        del_atten_ids = self.env['hr.attendance'].search([('emp_code', '=', str(lattendance[0])),('check_in', '=', atten_time)])
                                        if del_atten_ids:
                                            continue
                                        else:
                                            #create attendance value to hr.attendance table
                                            get_user_id = self.env['hr.employee'].search([('name','=',data_user[uid][1]),('emp_code', '=', str(lattendance[0]))]) 
                                            if get_user_id:
                                                data = hr_attendance.create({'employee_id': get_user_id.id,'emp_code':lattendance[0],'check_in':atten_time})
                                    else:
                                        employee = self.env['hr.employee'].create({'emp_code':str(lattendance[0]), 'name':data_user[uid][1]})
                                        data = hr_attendance.create({'employee_id': employee.id,'emp_code':lattendance[0],'check_in':atten_time})
                                else:
                                    pass
                                
        
                zk.enableDevice()
                zk.disconnect()
                return True
            else:
                raise ValidationError(_('Warning !'),_("Unable to connect, please check the parameters and network connections."))

    #Dowload attendence data regularly
    def schedule_download(self, ids=None):
        
>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
        if not self.ids:
            ids = self.search(ids).ids
            res = None
            try:
                res = self.browse(ids).download_attendance()
            except:
<<<<<<< HEAD
                raise ValidationError(('Warning !'), ("Machine with is not connected"))
            return res
=======
                raise ValidationError(('Warning !'),("Machine with is not connected" ))
            return res

>>>>>>> 906ebbdc1408c6890b79e764b16fac8283ef77f8
