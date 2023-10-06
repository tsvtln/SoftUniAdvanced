def concatenate(result='', *args, **kwargs):
    for string in args:
        result += string
    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)
    return result