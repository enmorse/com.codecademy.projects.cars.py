def make_car(manufacturer, model, **features):
    features['car_make'] = manufacturer
    features['car_model'] = model
    return features


build_car_one = make_car('ford', 'shelby gt500', color='black',
                         year=str(1967))
build_car_two = make_car('toyota', 'supra', color='orange',
                         year=str(1994))

print(build_car_one)
print(build_car_two)
