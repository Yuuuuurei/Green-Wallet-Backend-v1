import locale


def format_rupiah(amount):
    # Set the locale to Indonesian
    locale.setlocale(locale.LC_ALL, 'id_ID')

    # Format the number as currency
    formatted_amount = "Rp. " + locale.currency(amount, grouping=True, symbol=False)

    return formatted_amount