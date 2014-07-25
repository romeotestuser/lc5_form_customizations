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

class lc5_purchase_order_mod(osv.osv):
    _name = 'lc5.purchase.order.mod'
    _description = "Mode of Delivery"
    _columns = {
        'name':fields.char('Mode of Delivery', size=64),
}
lc5_purchase_order_mod()

class lc5_purchase_order(osv.osv):
    _inherit = 'purchase.order'
    _name="purchase.order"
    _columns = {
        #'project':fields.char('Project', size=64, required=False),
        'purchase_quotation_reference':fields.char('PQ Ref.', size=64, required=False),
        'mode_of_delivery_id':fields.many2one('lc5.purchase.order.mod','Mode of Delivery', required=False),
        #'delivery_lead_time_id':fields.many2one('lc5.sale.order.dlt','Delivery Lead Time', required=False),
        #'payment_method_id':fields.many2one('lc5.sale.order.pm','Payment Method', required=False),
        #'terms_of_payment_id':fields.many2one('lc5.sale.order.top','Terms of Payment', required=False),		
        #'intro':fields.text('Introduction', placeholder="Type your introduction..", required=False),
        #'closing':fields.text('Closing Message', placeholder="Type your closing message..", required=False),
        #'signature':fields.many2one('lc5.sale.order.signature','Signature', required=False),
        'prepared_by_id':fields.many2one('res.users', 'Prepared By', required=False), 
        #'verified_by_id':fields.many2one('res.users', 'Verified By', required=False), 
        'approved_by_id':fields.many2one('res.users', 'Approved By', required=False), 
    }
lc5_purchase_order()
