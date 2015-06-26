{
    'name': 'HR Employee Code',
    'version': '0.1',
    'author': 'Cubex Solutions',
    'website': 'http://www.cubex.solutions/',
    'category': 'Human Resources',
    'summary': """
    Simple Customization to fit a specific needs.
    """,
    'depends': ['hr_holidays', 'hr_payroll', 'hr_infraction', 'hr_schedule', 'hr_transfer', 'hr_wage_increment', ],
    'data':['hr_employee_code_view.xml', ],
    'installable': True,
    'auto_install': False,
}