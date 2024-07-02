def get_city_results(city: str, city_list: list[float]) -> str:
    """takes a tuple like ('Mumbai',[10.0,20.0,30.0,40.0]) and returns a string 
    like 'Mumbai;10.0;25.0;40.0' where the three numbers are the min, mean, and 
    max of the list."""
    city_min, city_mean, city_max = min(city_list), sum(city_list)/len(city_list), max(city_list)
    return f"{city};{city_min};{city_mean};{city_max}"


def create_cities_dict(cities:list[str])->dict[str,list[float]]:
    """ takes a list of form ['Mumbai;20','Mumbai;30','Mumbai;40','Mumbai;50']
    returns dict of form {'Mumbai':[10,20,30,40,50]}
    """
    cities_dict:dict[str,list[int]] = {}
    for row in cities:
        city, str_temperature = row.split(";")
        temperature = float(str_temperature)
        if city in cities_dict:
            cities_dict[city].append(temperature)
        else:
            cities_dict[city] = [temperature]
    return cities_dict

def get_results_list(cities_dict:dict[str,list[float]])->list[str]:
    return [get_city_results(city, cities_dict[city]) for city in cities_dict]


if __name__=="__main__":

    with open("test-measurements.txt", "r") as f:
        cities = f.readlines()

    print(cities)

    cities_dict = create_cities_dict(cities)
    print(cities_dict)
    results_list = get_results_list(cities_dict=cities_dict)
    print(results_list)
