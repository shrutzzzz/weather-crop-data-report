"""
This module defines the pytest fixture to be utilized by differnt test cases.
fixture allows us to mock differnt component of our application, 
which coudl be utlized at the time of testing different unit test cases without actually creating the resouce/ object.
"""

# importing built-in modules
import datetime
import pytest

from app import main
from app.main import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture(scope='module')
def client():

    app.config["TESTING"] = True
    app.testing = True

    # This creates an in-memory sqlite db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    
    main.db.init_app(app)
    
    client = app.test_client()
    
    with app.app_context():
        main.db.create_all()
        
        # Create an WXData type record and insert in DB
        wx_data = main.WXData(station_name="test_1",
                              date=datetime.datetime.strptime('19850101', '%Y%m%d'),
                              max_temp=20,
                              min_temp=10,
                              precipitation=200)
        
        main.db.session.add(wx_data)

        # Create an YLDData type record and insert in DB
        yld_data = main.YLDData(year=1985,
                                grain_yield=22250)
        
        main.db.session.add(yld_data)

        # Create an WXStats type record and insert in DB
        wxstats_data = main.WXStats(station_name="test_1",
                                    year=1985,
                                    avg_max_temp=20,
                                    avg_min_temp=10,
                                    total_precipitation=200)
        
        main.db.session.add(wxstats_data)
        
        main.db.session.commit()
    yield client
