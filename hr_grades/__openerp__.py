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


{
    'name': 'HR Employee Grading',
    'version': '0.1',
    'category': 'Human Resources',
    'summary': 'Trivial Grading System',
    'description': """
Trivial grading system
=======================================
In cases where HR Appraisals is too much, use this module for simple
grading and evaluation of employees.
""",
    'author': 'Cubex Solutions',
    'depends': ['hr'],
    'data': ['hr_grade.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
