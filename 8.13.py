def make_car(manufacturer, model, **options):
    car_dict = {'manufacturer': manufacturer.title(), 'model': model.title(), }
    for key, value in options.items():
        car_dict[key] = value
    return car_dict


my_subaru = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_subaru)

my_acura = make_car('acura', 'cx5', year=2014, color='white', structure='sedan')
print(my_acura)
