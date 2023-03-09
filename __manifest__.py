{
    'name': 'POS Session Wise Discount',
    'version': '16.0.1.0.0',
    'sequence': '-10',
    'category': 'pos',
    'summary': 'Set Session Wise Discount POS',
    'description': 'Set Session Wise Discount POS',

    'installation': True,
    'application': True,

    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/conf_settings_view.xml'
    ],
    'assets': {
       'point_of_sale.assets': [
           'pos_session_wise_discount/static/src/js/pos_session.js'
       ],
}
}