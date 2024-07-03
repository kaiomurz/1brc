import os
import sys
import time


def get_city_results(city: str, city_list: list[float]) -> str:
    """takes a tuple like ('Mumbai',[10.0,20.0,30.0,40.0]) and returns a string
    like 'Mumbai;10.0;25.0;40.0' where the three numbers are the min, mean, and
    max of the list."""
    city_min, city_mean, city_max = (
        min(city_list),
        sum(city_list) / len(city_list),
        max(city_list),
    )
    return f"{city};{city_min:.1f};{city_mean:.1f};{city_max:.1f}"


def create_cities_dict(cities: list[str]) -> dict[str, list[float]]:
    """takes a list of form ['Mumbai;20','Mumbai;30','Mumbai;40','Mumbai;50']
    returns dict of form {'Mumbai':[10,20,30,40,50]}
    """
    cities_dict: dict[str, list[int]] = {}
    for row in cities:
        city, str_temperature = row.split(";")
        temperature = float(str_temperature)
        if city in cities_dict:
            cities_dict[city].append(temperature)
        else:
            cities_dict[city] = [temperature]
    return cities_dict


def get_results_list(cities_dict: dict[str, list[float]]) -> list[str]:
    """takes a dict of form {'Mumbai':[10,20,30,40,50],...}
    returns list of form ['Mumbai;10.0;25.0;40.0',...]
    """

    return [get_city_results(city, cities_dict[city]) for city in cities_dict]

def get_measurements_path(size:str)->str:
    size_dir = {'3':'thousand', '6':'million', '9':'billion', 't':'test-measurements'}
    file_path = os.path.join(os.getcwd(), 'measurements')
    file_name = f"{size_dir[size]}.txt" if size in size_dir   else "test-measurements.txt" 
    return f"{file_path}/{file_name}"

if __name__ == "__main__":

    start_time = time.time()
    measurements_path = get_measurements_path(sys.argv[1])

    with open(measurements_path, "r") as f:
        cities = f.readlines()

    cities_dict = create_cities_dict(cities)
    results_list = get_results_list(cities_dict=cities_dict)

    with open("onebrc_results.txt", "w") as f:
        for line in results_list:
            f.write(f"{line}\n")

    print(f"time taken:{time.time()-start_time:.2f}")