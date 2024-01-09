def oxford_comma(items):
    '''converts a list into a string using the Oxford Comma'''
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

