{
    'name':"Cat",
    'summary':"""My pet model""",
    'description':"""Managing pet information""",
    'author':"quochuy",
    'website':"https://www.odoo.com/app/notes",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
        'wizard/batch_update.xml',
        'views/res_config_settings_views.xml',
        'views/pet_male.xml',
        # 'views/templates.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': {
    #         '/mypet/static/src/js/bold.js',
    #     },
    # },
    'installable': True,
    'application': True,
}