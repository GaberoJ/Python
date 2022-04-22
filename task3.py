def students_gen():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]

    classes = [
        '9А', '7В', '9Б', '9В', '8Б', '10А'
    ]

    if len(classes) < len(tutors):
        while len(classes) != len(tutors):
            classes.append('None')

    tuples = ((tutors[i], classes[i]) for i in range(len(tutors)))
    for i in range(len(tutors)):  # for i in range(len(tutors) + 1) - покажет, что генератор истощен
        print(next(tuples))

    return type(tuples)


print(students_gen())
