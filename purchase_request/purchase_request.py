# -*- coding: utf-8 -*-
##############################################################################
#
#    Cubex Solutions, a module for CruzeERP and compatible with OpenERP v7.0
#    Copyright (C) 2010-Today Cubex Solutions (<http://www.cubexco.com>).
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
from openerp.tools.translate import _

class purchase_request(osv.osv):
    _name = 'purchase.request'
    _description = 'Purchase Request'
    _columns = {
        'name': fields.char('Name', required=True,),
        'user_id': fields.many2one('res.users', string="Requested By", required=True, ondelete="cascade"),
        'create_date': fields.datetime('Created', readonly=True),
        'create_uid': fields.many2one('res.users', string='Creator', readonly=True),
        'request_items': fields.text(string='Requested Items', required=True),
        'request_reason': fields.text(string='Request Reason', required=True),
        'required_date': fields.datetime('Required Date'),
        'notes': fields.text(string='Notes'),
        'priority': fields.selection([('low','Low'),
            ('medium','Medium'),
            ('high','High'),
            ('urgent','Urgent')],
            string='Priority'),
        'state':fields.selection([
            ('new','New'),
            ('confirmed','Confirmed'),
            ('refused','Refused'),
            ('canceled','Canceled')
            ],
            string='State',)
        }
    _defaults = {
        'user_id': lambda obj, cr, uid, context: uid,
        'required_date': fields.datetime.now,
        'name': lambda self, cr, uid, context: self.pool['ir.sequence'].get(cr, uid, 'purchase.request', context=context) or '/',
        }
    _sql_constraints = [
        ('name_uniq', 'unique(name, company_id)', 'Order Reference must be unique per Company!'),
    ]
purchase_request()