from collections import Counter
import plotly
plotly.offline.init_notebook_mode(connected=True)

class Driver:
    _all = []
    _count = 0
    list_names = []
    list_fleet_makes = []
    list_fleet_models = []

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model

        Driver._all.append(self)
        Driver.list_names.append(name)
        Driver.list_fleet_makes.append(car_make)
        Driver.list_fleet_models.append(car_model)
        Driver._count += 1

    @classmethod
    def fleet_size(cls):
        return Driver._count

    @classmethod
    def driver_names(cls):
        return Driver.list_names

    @classmethod
    def fleet_makes(cls):
        return Driver.list_fleet_makes

    @classmethod
    def fleet_models(cls):
        return Driver.list_fleet_models

    @classmethod
    def fleet_makes_count(cls):
        count = dict(Counter(Driver.list_fleet_makes))
        x = list(count.keys())
        y = list(count.values())
        trace = {'type': 'bar', 'x': x, 'y': y}
        plotly.offline.iplot([trace])

    @classmethod
    def fleet_models_count(cls):
        count = dict(Counter(Driver.list_fleet_models))
        x = list(count.keys())
        y = list(count.values())
        trace = {'type': 'bar', 'x': x, 'y': y}
        plotly.offline.iplot([trace])

    @classmethod
    def percent_of_fleet(cls, make):
        count = dict(Counter(Driver.list_fleet_makes))
        print(count)
        main_make_count = count[make]
        total = len(Driver.list_fleet_makes)
        return str(main_make_count*100/total)+'%'


Driver("Helga Pataki", "Toyota", "Camry")
Driver("Arnold Shortman", "Toyota", "Highlander")
Driver("Gerald Johanssen", "Toyota", "Camry")
Driver("Robert 'Big Bob' Pataki", "Honda", "Pilot")
Driver("Grandpa Phil", "Jeep", "Grand Cherokee")
Driver("Rhonda Wellington Lloyd", "Kia", "Sonata")
Driver("Phoebe Heyerdahl", "Honda", "Civic")
