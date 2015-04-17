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