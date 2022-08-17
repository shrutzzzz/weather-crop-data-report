## Steps to run the app
1. Clone the repository
2. Run the following command: <br>
```git clone https://github.com/shrutzzzz/weather-crop-data-report.git``` <br>
3. Go to src directory: <br>
```cd weather-crop-data-report/src``` <br>
4. Install dependencies <br>
```pip install -r app/requirements.txt``` <br>
5. Initialize the DB <br>
```flask --app app/main.py initdb``` <br>
6. Run the Flask app <br>
```python app/main.py``` <br>
7. Ingest the data <br>
```curl -X POST http://127.0.0.1:5000/api/ingest``` <br>
8. Calculate and Ingest the Weather Stats <br>
```curl -X POST "http://127.0.0.1:5000/api/cal_stats"``` <br>
9. Get the Weather Data <br>
```curl -X GET "http://127.0.0.1:5000/api/weather"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?station_name=USC00134063&date=19850101&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?station_name=USC00134063&date=19850101"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?station_name=USC00134063&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?date=19850101&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?station_name=USC00134063"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?date=19850101"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather?page=1"``` <br>
10. Get the Yield Data <br>
```curl -X GET "http://127.0.0.1:5000/api/yield?year=1985&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/yield?year=1985"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/yield?page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/yield"``` <br>
11. Get the Weather Stats Data <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?station_name=USC00134063&year=1985&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?station_name=USC00134063&year=1985"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?station_name=USC00134063&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?year=1985&page=1"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?station_name=USC00134063"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?year=1985"``` <br>
```curl -X GET "http://127.0.0.1:5000/api/weather/stats?page=1"``` <br>
12. Run the pytest test cases <br>
```python -m pytest tests``` <br>
