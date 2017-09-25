# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2010-2017 StarYAP All Rights Reserved.
#                         Pablo Cardoza Magallón <pablocm83@gmail.com>
#                         Yunier Pérez Torres <yunierstar@gmail.com>


{
    'name' : 'Cuba - Accounting for TCP',
    'version' : '2.0',
    'author' : 'StarYAP',
    'website' : 'http://',
    'category': 'Localization',
    'sequence': 2,
    'summary': 'Cuban charts of accounts for TCP',
    'description': """
Cuban charts of accounts for TCP.
========================================

    * Defines the following chart of account templates:
        * Cuban general chart of accounts
        * Cuban general chart of accounts for small and medium companies
        * Cuban general chart of accounts for associations
    * Defines templates for sale and purchase
    * Defines tax code templates
    * Defines fiscal positions for cuban fiscal legislation
""",
    'depends' : [
        'account'
    ],
    'data' : [
        'data/res_currency_data.yml',
        'data/res_country_state_data.xml',
        'data/account_account_type_data.xml',
        'data/l10n_cu_tcp_chart_data.xml',
        'data/account_account_template_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
    'demo': [

    ],
    'test': [

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
