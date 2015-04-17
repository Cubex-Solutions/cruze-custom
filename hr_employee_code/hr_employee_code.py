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