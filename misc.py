def as_currency(amount):
    if amount >= 0:
        return '${:,.0f}'.format(amount)
    else:
        return '-${:,.0f}'.format(-amount)

def is_number(s):
    s = s.replace(',','')
    try:
        float(s)
        return True
    except ValueError:
        return False

def as_float(s):
    s = s.replace(',','')
    return float(s)
