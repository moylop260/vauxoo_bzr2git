#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Vauxoo C.A.           
#    Planified by: Nhomar Hernandez
#    Audited by: Vauxoo C.A.
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

from osv import fields, osv
import tools
from tools.translate import _
from tools import config
import netsvc
import decimal_precision as dp
import datetime

class account_invoice(osv.osv):
    
    _inherit = 'account.invoice'
    
    def default_get(self, cr, uid, fields, context=None):
        """ Get default values
        Give date and time of invoice creation
        """
        if context is None:
            context = {}
        res = super(account_invoice, self).default_get(cr, uid, fields, context=context)
        res.update({'date_compute':datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')})


        return res
        
    _columns = {
    'date_compute':fields.datetime('Invoice Date', help="Date to compute the product cost in the invoice"),
    }
    
    
account_invoice()
