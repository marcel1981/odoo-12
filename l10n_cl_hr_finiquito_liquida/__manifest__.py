# -*- coding: utf-8 -*-
###################################################################################
#
#    Intellego-BI.com
#    Copyright (C) 2017-TODAY Intellego Business Intelligence S.A.(<http://www.intellego-bi.com>).
#    Author: Rodolfo Bermúdez Neubauer(<https://www.intellego-bi.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
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
###################################################################################
{
    'name': 'RRHH Chile - Liquidación Finiquito Laboral',
    'version': '12.0.1.0.0',
    'summary': """Cálculo de conceptos de Finiquito Laboral """,
    'author': 'Intellego-BI.com',
    'company': 'Intellego-BI.com',
    'website': 'https://www.Intellego-BI.com',
    'depends': ['base', 'mail', 'hr_payroll', 'l10n_cl_hr', 'l10n_cl_hr_employee_extend', 'l10n_cl_hr_finiquito_solicita'],
    'category': 'Human Resources',
    'maintainer': 'Intellego-BI.com',
    'data': ['views/employee_gratuity_view.xml',
             'views/gratuity_sequence.xml',
             'views/final_settlements.xml',
             'data/salary_rule_settle.xml',
             'security/ir.model.access.csv'],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}