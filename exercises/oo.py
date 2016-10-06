class Circle():
    """Implementation av klassen `Circle`.

    Klassen ska ha attributen `radius` och `color`. Attributet `radius` ska
    vara obligatioriskt och attributet `color` ska ha ett standardvärdet `red`.

    Klassen ska ha metoderna `diameter` och `area` som returnerar
    lämpliga värden.

    Implementera den magiska metoden `__repr__` så att ett cirkel-objekt får
    representationen `<Circle: 10>` om den har radien 10.
    """
    pass


class Rectangle():
    """Implementation av klassen `Rectangle`.

    Klassen ska ha attributen `width` och `height`. Båda attributen ska vara
    obligatoriska vid skapandet av objekt.

    Klassen ska ha metoderna `area` och `perimiter` som returnerar
    lämpliga värden.

    Implementera den magiska metoden `__repr__` så att ett rektangel-objekt får
    representationen `<Rectangle: 10, 20>` om den har bredden 10 och höjden 20.

    Implementera även den magisa metoden `__eq__` så att två rectanglar anses
    lika om de har samma proportioner.
    """
    pass


class Employee():
    """Implementation av klassen `Employee`.

    Klassen ska ha attributen `id`, `name` och `salary`. Attributen `name` och
    `salary` ska vara obligatoriska och `id` ska få nästa lediga heltal (med
    start på 0). `id` ska alltså inte anges vid skapandet av nya objekt.

    Klassen ska metoder `raise_salary` med löneökningen angiven som ett
    antal procent.

    Klassen ska även ha en metod `annual_salary` som returnerar den antälldes
    årslön (`salary`-attributet innehåller månadslönen.)

    Metoderna __str__ och __repr__ ska finnas, se testerna för exempel på
    hur deras utdata ska se ut.
    """
    pass
