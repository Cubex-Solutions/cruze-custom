from openerp.osv import fields, osv


class event_registeration(osv.Model):
    _name = "event.registration"
    _inherit = "event.registration"

    def get_emp_obj(self, cr, uid, employee_code, context=None):
        emp_pool = self.pool.get('hr.employee')
        employee_id = emp_pool.search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
        employee_partner_id = emp_pool.browse(cr, uid, employee_id, context=context)
        return employee_id, employee_partner_id

    def _get_employee_id(self, cr, uid, ids, field_names, args, context=None):
        res = {}
        event_objs = self.browse(cr, uid, ids, context=context)
        emp_pool = self.pool.get('hr.employee')
        for event in event_objs:
            res[event.id] = False
            if event.employee_code:
                employee_id = emp_pool.search(cr, uid, [('employee_code', '=', event.employee_code)], context=context)[0]
            else:
                employee_id = False

            res[event.id]= employee_id
        return res

    def onchange_employee_code(self, cr, uid, ids, employee_code, context):
        if employee_code:
            emp_pool = self.pool.get('hr.employee')
            employee_id = emp_pool.search(cr, uid, [('employee_code', '=', employee_code)], context=context)[0]
            employee_partner_id = emp_pool.browse(cr, uid, employee_id, context=context)
            if employee_partner_id.address_home_id:
                return {'value':
                            {'employee_id': employee_id, 'partner_id': employee_partner_id.address_home_id.id, },
                        }
            else:
                raise osv.except_osv('Warning!', 'You are trying to add an Employee who has no Home Address!')
        else:
            return {'value':
                        {'employee_id': False}
                    }

    _columns = {
        'employee_code': fields.integer(string="Employee Code", required=True, ),
        'employee_id': fields.function(_get_employee_id, type='many2one', relation='hr.employee', string='Employee', store=True, ),
    }