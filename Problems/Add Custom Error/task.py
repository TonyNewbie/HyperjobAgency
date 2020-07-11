def add_custom_errors(form):
    if not form.is_valid():
        return
    code_data = form.data.get('code')
    if not code_data.startswith('2020'):
        form.add_error('code', 'promo code is expired')
    if not code_data.endswith('django'):
        form.add_error('code', 'checksum is invalid')
