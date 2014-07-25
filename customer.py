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

class lc5_partner_nature_business(osv.osv):
    _name = 'lc5.partner.nature.business'
    _description = "Nature of Business"
    _columns = {
        'name':fields.char('Business', size=64),
       }
lc5_partner_nature_business()

class lc5_partner_organization(osv.osv):
    _name = 'lc5.partner.organization'
    _description = "Organization"
    _columns = {
        'name':fields.char('Organization', size=64),
       }
lc5_partner_organization()

class lc5_partner_references(osv.osv):
    _name = 'lc5.partner.references'
    _description = "References"
    _columns = {
        'name':fields.char('Contact Name', size=64),
        'company':fields.char('Company', size=64),
        'address':fields.char('Address', size=64),
        'tel_no':fields.char('Tel No', size=64),
        'fax_no':fields.char('Fax No', size=64),
        'note':fields.text('Note'),
        'partner_id':fields.many2one('res.partner','Partner', ondelete='cascade'),
       }
lc5_partner_references()

class lc5_partner(osv.osv):
    _inherit = "res.partner"
    _name="res.partner"
    _columns = {
        'nationality':fields.char('Nationality', size=64, required=False),
        'nature_of_business_id':fields.many2one('lc5.partner.nature.business','Nature of Business', required=False),
        'organization_id':fields.many2one('lc5.partner.organization','Organization', required=False),
        'reference_ids':fields.one2many('lc5.partner.references','partner_id','Reference', required=False),
}
lc5_partner()
