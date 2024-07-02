
def get_city_results(city:str, results:list[int])->str:
    city_min, city_mean, city_max = min(results), sum(results)/len(results), max(results)
    return f"{city};{city_min};{city_mean};{city_max}"

