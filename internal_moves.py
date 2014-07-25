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
		  
class lc5_stock_picking(osv.osv):
    _inherit="stock.picking"
    _name="stock.picking"
    _name="stock.picking"
    _columns= {
        'transfer_request_reference':fields.char('Transfer Ref.', size=64, required=False),
        'delivery_vehicle_id':fields.many2one('lc5.delivery.order.vehicle','Delivery Vehicle', required=False),
        'driver_id':fields.many2one('lc5.delivery.order.driver','Driver', required=False),
        'people_in_charge':fields.text('People in charge', placeholder="People involved in the delivery..", required=False),
        'prepared_by_id':fields.many2one('res.users', 'Prepared By', required=False), 
        'verified_by_id':fields.many2one('res.users', 'Verified By', required=False), 
        'approved_by_id':fields.many2one('res.users', 'Approved By', required=False), 		
        'delivery_remarks':fields.text('Delivery Remarks', placeholder="Add a remark..", required=False),
	}
lc5_stock_picking() 
