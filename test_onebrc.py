from hamcrest import assert_that, equal_to
from onebrc import get_city_results

def test_get_city_results():
    city = 'Mumbai'
    results = [10.0,20.0,30.0,40.0]
    city_result = "Mumbai;10.0;25.0;40.0"
    returned_city_result = get_city_results(city=city, results=results) 
    assert_that(returned_city_result, equal_to(city_result))
