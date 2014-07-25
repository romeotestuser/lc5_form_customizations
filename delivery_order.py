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

class lc5_delivery_order_vehicle(osv.osv):
    _name = 'lc5.delivery.order.vehicle'
    _description = "Delivery Vehicle"
    _columns = {
        'name':fields.char('Delivery Vehicle', size=64),
}

class lc5_delivery_order_driver(osv.osv):
    _name = 'lc5.delivery.order.driver'
    _description = "Driver"
    _columns = {
        'name':fields.char('Driver', size=64),
}
class lc5_stock_picking(osv.osv):
    _inherit="stock.picking"
    _name="stock.picking"
    _columns= {
        'project':fields.char('Project', size=64, required=False),
        'sales_invoice_reference':fields.char('SI Ref.', size=64, required=False),
        'sales_order_reference':fields.char('SO Ref.', size=64, required=False),
        'purchase_order_reference':fields.char('PO Ref.', size=64, required=False),
        'delivery_vehicle_id':fields.many2one('lc5.delivery.order.vehicle','Delivery Vehicle', required=False),
        'driver_id':fields.many2one('lc5.delivery.order.driver','Driver', required=False),
        'people_in_charge':fields.text('People in charge', placeholder="People involved in the delivery..", required=False),
        'prepared_by_id':fields.many2one('res.users', 'Prepared By', required=False), 
        'verified_by_id':fields.many2one('res.users', 'Verified By', required=False), 
        'approved_by_id':fields.many2one('res.users', 'Approved By', required=False),         
        'delivery_remarks':fields.text('Delivery Remarks', placeholder="Add a remark..", required=False),
    }
	
class lc5_stock_picking_out(osv.osv):
    _inherit="stock.picking.out"
    _name="stock.picking.out"
    _columns= {
        'project':fields.char('Project', size=64, required=False),
        'sales_invoice_reference':fields.char('SI Ref.', size=64, required=False),
        'sales_order_reference':fields.char('SO Ref.', size=64, required=False),
        'purchase_order_reference':fields.char('PO Ref.', size=64, required=False),
        'delivery_vehicle_id':fields.many2one('lc5.delivery.order.vehicle','Delivery Vehicle', required=False),
        'driver_id':fields.many2one('lc5.delivery.order.driver','Driver', required=False),
        'people_in_charge':fields.text('People in charge', placeholder="People involved in the delivery..", required=False),
        'prepared_by_id':fields.many2one('res.users', 'Prepared By', required=False), 
        'verified_by_id':fields.many2one('res.users', 'Verified By', required=False), 
        'approved_by_id':fields.many2one('res.users', 'Approved By', required=False), 		
        'delivery_remarks':fields.text('Delivery Remarks', placeholder="Add a remark..", required=False),
	}
