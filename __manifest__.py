
{
	'name': 'Modulo PG',
	
	'version': '12.0',
       
	'summary': 'Custom PG',
	'description': """
Varios Ajuste para PG:
======================
	* Este módulo es para la empresa PG.
	
	""",
	'depends': [
		
		'l10n_co_tax_extension','l10n_co_e-invoice','l10n_co_suport_doc'
	],
	'data': [
		
		'views/invoice_report_custom.xml',
		
	],
	'installable': True,
	'application': True,
	'auto_install': False,
}
