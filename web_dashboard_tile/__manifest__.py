# -*- coding: utf-8 -*-
# © 2010-2013 OpenERP s.a. (<http://openerp.com>).
# © 2014 initOS GmbH & Co. KG (<http://www.initos.com>).
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Dashboard Tile",
    "summary": "Add Tiles to Dashboard",
    "version": "12.0.1.0.0",
    "depends": [
        'web',
        'board',
        'mail',
        'web_widget_color',
    ],
    'author': 'initOS GmbH & Co. KG, '
              'GRAP, '
              'Odoo Community Association (OCA)',
    "category": "web",
    'license': 'AGPL-3',
    'contributors': [
        'initOS GmbH & Co. KG',
        'GRAP',
        'Iván Todorovich <ivan.todorovich@gmail.com>'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/rules.xml',
        'data/res_groups.xml',
        'data/tile_tile.xml',
        'views/tile.xml',
        'views/templates.xml',
        
    ],
    'demo': [

    ],
    'qweb': [
        'static/src/xml/custom_xml.xml',
    ],
}
