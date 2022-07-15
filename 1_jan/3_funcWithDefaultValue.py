def person(lname='Abdol', fname='Hamid', city='Tabrizi', age='30'):
    print(f"Hello, I'm {fname} {lname} .")
    print(f"I'm from {city} .")
    print(f"I'm {age} years old .")
    print('-'*60)

person('Rouz', 'Peiman', 'Mashhad', '31')
person('Rouz', 'Peiman', 'Mashhad')
person('Rouz', 'Peiman')
person('Rouz')
person()
person(city='Tehran')
