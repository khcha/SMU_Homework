import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta
import dateutil.relativedelta

from flask import Flask, jsonify

import datetime as dt


engine = create_engine("sqlite:///C:/Users/Kyoo Ha Cha/Desktop/SMUGitlab/SMU_Homework/Unit_10_Advanced-Data-Storage-and-Retrieval/Instructions/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# Flask Setup

app = Flask(__name__)


# Flask Routes


@app.route("/")
def welcome():
    """List all available api routes."""
    
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"1. /api/v1.0/precipitation<br/>"
        f"**List of prior year rain totals from all stations**<br/>"
        f"<br/>"
        f"2. /api/v1.0/stations<br/>"
        f"**List of Stations**<br/>"
        f"<br/>"
        f"3. /api/v1.0/tobs<br/>"
        f"**List of the last 12 months of precipitation data**<br/>"
        f"<br/>"
        f"4. /api/v1.0/start<br/>"
        f"**List of MIN/AVG/MAX temperature for all dates greater than and equal to the start date**<br/>"
        f"<br/>"
        f"5. /api/v1.0/start/end<br/>"
        f"**List MIN/AVG/MAX temperature for dates between the start and end date**<br/>"

    )


# Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_date= datetime.strptime(last_date, '%Y-%m-%d')
    first_date = last_date-timedelta(days=365)

    old_prcp = (session.query(Measurement.date, Measurement.prcp)
                .filter(Measurement.date <= last_date)
                .filter(Measurement.date >= first_date)
                .order_by(Measurement.date).all())
    
    precip = {date: prcp for date, prcp in old_prcp}
    
    return jsonify(precip)


# Stations
@app.route('/api/v1.0/stations')
def stations():
    stations_all = session.query(Station.station).all()
    return jsonify(stations_all)

# Tobs
@app.route('/api/v1.0/tobs') 
def tobs():  
    most_active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
            group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc()).all()
    most_active_station = [i[0] for i in most_active_stations][0]

    last_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_date= datetime.strptime(last_date, '%Y-%m-%d')
    first_date = last_date-timedelta(days=365)

    lastyear = (session.query(Measurement.date,Measurement.tobs)
                .filter(Measurement.station == most_active_station)
                .filter(Measurement.date <= last_date)
                .filter(Measurement.date >= first_date)
                .order_by(Measurement.tobs).all())
    
    return jsonify(lastyear)

# Start
@app.route("/api/v1.0/<start>") 
def start_only(start):
    start_date = dt.date(2012, 2, 28)
    
    start_only = session.query(Measurement.date,func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
             .filter(Measurement.date >= start_date) \
             .group_by(Measurement.date).all()

    return jsonify(start_only)

# Start & End
@app.route('/api/v1.0/<start>/<end>') 
def start_end(start, end):
    start_date = dt.date(2012, 2, 28)
    end_date = dt.date(2012, 3, 5)
    start_end = session.query(Measurement.date,func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)) \
             .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date) \
             .group_by(Measurement.date).all()
    return jsonify(start_end)

if __name__ == '__main__':
    app.run(debug=True)