"""
This module contains multiple test cases to test the 3 main GET API defined in application to retrive the data from 3 different data models in json format
"""

def test_weather(client):
    """
    This function test the /api/weather api without passing any query parameter
    """
    weather = client.get("/api/weather")
    
    assert {"station_name": "test_1", "date": "1985-01-01T00:00:00", "max_temp": 20, "min_temp": 10, "precipitation": 200} == weather.json[0]


def test_yield_1(client):
    """
    This function test the /api/yield api with year=1985 as query parameter
    """
    yield_ = client.get("/api/yield?year=1985")
    
    assert {"year": 1985, "grain_yield": 22250} == yield_.json[0]


def test_yield_2(client):
    """
    This function test the /api/yield api with year=1986 as query parameter
    """
    yield_ = client.get("/api/yield?year=1986")
    
    assert [] == yield_.json

def test_w_stats(client):
    """
    This function test the /api/weather/stats api without passing any query parameter
    """
    w_stats = client.get("/api/weather/stats")
    
    assert {"station_name": "test_1", "year": 1985, "avg_max_temp": 20, "avg_min_temp": 10, "total_precipitation": 200} == w_stats.json[0]
