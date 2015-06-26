# -*- coding: utf-8 -*-
##############################################################################
#
#    CruzeERP Module, compatible with OpenERP 7.0
#    Cubex Solutions © 2011 - Today.
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

from openerp.osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    _columns = {
        'insurance_grade': fields.selection([
            ('grade_a','Grade A'),
            ('grade_b','Grade B'),
            ('grade_c','Grade C')],
            string="Insurance Grade",
            required=True,),
        'ssn_date': fields.date(string="SSN Start"),
        'ssn_file': fields.integer(string="SSN File No"),
        'gov_insurance': fields.boolean(string="Government Insurance"),
    }