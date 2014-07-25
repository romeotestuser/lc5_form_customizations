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

from openerp.osv import fields, osv
from openerp.tools.translate import _

class lc5_account_invoice(osv.osv):
    _inherit = "account.invoice"
    _name="account.invoice"
    _columns = {
        'project':fields.char('Project', size=64, required=False),
        'delivery_receipt_reference':fields.char('DR Ref.', size=64, required=False),
        'purchase_order_reference':fields.char('PO Ref.', size=64, required=False),
        'warranty_id':fields.many2one('lc5.sale.order.warranty','Warranty', required=False),
        'delivery_lead_time_id':fields.many2one('lc5.sale.order.dlt','Delivery Lead Time', required=False),
        'payment_method_id':fields.many2one('lc5.sale.order.pm','Payment Method', required=False),
        'terms_of_payment_id':fields.many2one('lc5.sale.order.top','Terms of Payment', required=False),		
        'prepared_by_id':fields.many2one('res.users', 'Prepared By', required=False), 
        'verified_by_id':fields.many2one('res.users', 'Verified By', required=False), 
        'approved_by_id':fields.many2one('res.users', 'Approved By', required=False), 
    }
lc5_account_invoice()
