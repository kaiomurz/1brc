from hamcrest import assert_that, equal_to
from onebrc import get_city_results, create_cities_dict


def test_get_city_results():
    city = "Mumbai"
    city_list = [10.0, 20.0, 30.0, 40.0]
    expected_city_result = "Mumbai;10.0;25.0;40.0"
    returned_city_result = get_city_results(city=city, city_list=city_list)
    assert_that(returned_city_result, equal_to(expected_city_result))


def test_create_cities_dict():
    cities = [
        "Mumbai;20.0",
        "Mumbai;30.0",
        "Mumbai;40.0",
        "Mumbai;50.0",
        "Oman;30.5",
        "Oman;40.5",
        "London;20.5",
    ]
    expected_cities_dict = {
        "Mumbai": [20.0, 30.0, 40.0, 50.0],
        "Oman": [30.5, 40.5],
        "London": [20.5],
    }

    returned_cities_dict = create_cities_dict(cities=cities) 
    assert_that(returned_cities_dict, equal_to(expected_cities_dict))
