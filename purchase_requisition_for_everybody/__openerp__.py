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
{
    'name' : 'Purchase Requisition for Everybody',
    'version' : '1.0',
    'author' : 'Vauxoo',
    'category' : 'Security',
    'description' : """
Records Rule for Purchase_Requisition Module
============================================

Created 2 groups which are Requisition / User and Requisition / Manager and new purchase requisition menu to separate from purchase menu

With Requisition / User we can see only your own requisition and modify these
With Requisition / Manage  we can see whole requisition and modify these

You need any of those 2 groups for you can see the new purchase requisition menu

    """,
    'website': 'http://www.vauxoo.com',
    'images' : [],
    'depends' : ['base','purchase','purchase_requisition'],
    'data': [
        'security/requisition_security.xml',
        'view/purchase_requisition_view.xml',
        'security/ir.model.access.csv',
    ],
    'js': [
    ],
    'qweb' : [
    ],
    'css':[
    ],
    'demo': [
],
    'test': [
],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
