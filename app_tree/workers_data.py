import random

from .models import *


def generator_names():
    lst = ['Liam', 'Noah', 'Oliver', 'Elijah',
           'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Kai',
           'Christian', 'Landon', 'Colton', 'Roman', 'Axel', 'Brooks',
           'Jonathan', 'Robert', 'Jameson']

    return random.choice(lst)


def add_to_database():
    for i in range(1000):
        manager_one = Workers.objects.create(name=generator_names(),
                                             job_title='Boss',
                                             salary=random.uniform(100, 200))
        for j in range(1):
            manager_two = Workers.objects.create(name=generator_names(),
                                                 job_title='First Manager',
                                                 salary=random.uniform(90, 100),
                                                 parent=manager_one)
            for j in range(1):
                manager_three = Workers.objects.create(name=generator_names(),
                                                       job_title='Second Manager',
                                                       salary=random.uniform(80, 90),
                                                       parent=manager_two)
                for b in range(1):
                    manager_four = Workers.objects.create(name=generator_names(),
                                                          job_title='Third Manager',
                                                          salary=random.uniform(70, 80),
                                                          parent=manager_three)
                    for l in range(1):
                        Workers.objects.create(name=generator_names(),
                                               job_title='Fourth Manager',
                                               salary=random.uniform(60, 70),
                                               parent=manager_four)
