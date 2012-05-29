#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) Vauxoo (<http://vauxoo.com>).
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
{
    "name" : "Cost Structure",
    "version" : "0.1",
    "depends" : ['account',"stock",'product','sale','purchase','invoice_date_time'],
    "author" : "Vauxoo",
    "description" : """
    Module that performs a calculation of average cost in products, 
    this module performs a search of all movements made by you for goods 
    and are assigned to cost structure
    """,
    "website" : "http://vauxoo.com",
    "category" : "Generic Modules",
    "init_xml" : ['data/data_load.xml'],
    "demo_xml" : [],
    "test": [ ],
    "update_xml" : [
    'security/cost_structure_security.xml',
    'security/ir.model.access.csv',
    'wizard/compute_cost_view.xml',
    'view/cost_structure.xml',
    'view/report_cost.xml',
    'view/product_view.xml',
    'view/sale_view.xml',
    'workflow/sale_workflow.xml',
    
    
    
    
    ],
    "active": False,
    "installable": True,
}
