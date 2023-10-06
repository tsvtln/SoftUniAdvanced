def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]
    result = sorted(persons.items(), key=lambda x: x[0])
    result_2 = []
    for name, age in result:
        result_2.append(f"{name} is {age} years old.")
    return "\n".join(result_2)



'''test print'''
print(age_assignment("Peter", "George", G=26, P=19))