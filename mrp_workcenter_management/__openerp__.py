#!/usr/bin/python
# -*- encoding: utf-8 -*-
###############################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
# Credits######################################################
#    Coded by: Yanina Aular <yanina.aular@vauxoo.com>
#              Katherine Zaoral <katherine.zaoral@vauxoo.com>
#    Planified by: Yanina Aular <yanina.aular@vauxoo.com>
#    Audited by: Humberto Arocha <humbertoarocha@gmail.com>
###############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

{
    "name": "MRP Workcenter Management",
    "version": "1.0",
    "author": "Vauxoo",
    "website": "http://vauxoo.com",
    "category": "MRP",
    "description": """

MRP Management Workcenter.
==========================

This module adds a better management of Work Centers on Manufacturing module.
List of new functionalities:

- adds a new menuitem at **Manufacturing** > **Manufacturing** > **Work Centers**  that shows the work centers registered.

 """,
    "depends": ["base", "mrp", "mrp_operations"],
    "data": [
        "view/mrp_workcenter_view.xml",
    ],
    "js": [],
    "qweb": [],
    "css": [],
    "demo": [],
    "test": [],
    "installable": True,
    "active": False,
    }
