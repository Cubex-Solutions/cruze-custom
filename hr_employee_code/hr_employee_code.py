from openerp.osv import fields, osv


class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    _sql_constraints = [
        ('employee_code_uniq', 'unique(employee_code)', 'The Code of the Employee must be unique!'),
    ]


class hr_holidays(osv.Model):
    _name = 'hr.holidays'
    _inherit = 'hr.holidays'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", ),
    }

    def _get_default_code(self, cr, uid, context=None):
        emp_id=self._employee_get(cr, uid, context=None)
        if emp_id:
            return self.pool.get('hr.employee').browse(cr, uid, emp_id, context=context).employee_code
        return 0

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

    _defaults = {
        'employee_code': _get_default_code,
    }


class hr_contract(osv.Model):
    _name = 'hr.contract'
    _inherit = 'hr.contract'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }


class hr_payslip(osv.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_schedule(osv.osv):
    _name = 'hr.schedule'
    _inherit = 'hr.schedule'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class schedule_detail(osv.osv):
    _name = 'hr.schedule.detail'
    _inherit = 'hr.schedule.detail'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_schedule_request(osv.osv):
    _name = 'hr.schedule.request'
    _inherit = 'hr.schedule.request'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_schedule_alert(osv.osv):
    _name = 'hr.schedule.alert'
    _inherit = 'hr.schedule.alert'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class schedule_ot(osv.Model):
    _name = 'hr.schedule.ot'
    _inherit = 'hr.schedule.ot'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_attendance(osv.osv):
    _name = 'hr.attendance'
    _inherit = 'hr.attendance'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_transfer(osv.Model):
    _name = 'hr.department.transfer'
    _inherit = 'hr.department.transfer'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class wage_increment(osv.osv):
    _name = 'hr.contract.wage.increment'
    _inherit= 'hr.contract.wage.increment'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_infraction(osv.Model):
    _name = 'hr.infraction'
    _inherit = 'hr.infraction'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_infraction_action(osv.Model):
    _name = 'hr.infraction.action'
    _inherit = 'hr.infraction.action'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

class hr_warning(osv.Model):
    _name = 'hr.infraction.warning'
    _inherit = 'hr.infraction.warning'

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
    }

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            employee_id = self.pool.get('hr.employee').search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            return {'value':
                        {'employee_id': employee_id}
                    }
        else:
            return {'value':
                        {'employee_id': False}
                    }

