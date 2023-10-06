def even_odd_filter(**kwargs):
    for key, numbers in kwargs.items():
        if key == 'even':
            kwargs[key] = [x for x in numbers if x % 2 == 0]
        else:
            kwargs[key] = [x for x in numbers if x % 2 != 0]
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
