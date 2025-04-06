# Import the dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
import webbrowser

#################################################
# Database Setup
#################################################

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Homepage route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Start a session
    session = Session(engine)

    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()

    # Close the session
    session.close()

    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Start a session
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()

    # Close the session
    session.close()

    # Convert the results to a list
    station_list = [station[0] for station in results]
    return jsonify(station_list)

# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    # Start a session
    session = Session(engine)

    # Find the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Find the most recent date and calculate the date one year ago
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query the TOBS data for the most active station in the last year
    results = session.query(Measurement.tobs).filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= year_ago).all()

    # Close the session
    session.close()

    # Convert the results to a list
    tobs_list = [tobs[0] for tobs in results]
    return jsonify(tobs_list)

# Start date route
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Start a session
    session = Session(engine)

    # Query min, avg, and max temps from the start date onwards
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    # Close the session
    session.close()

    # Convert the results to a dictionary
    temps = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temps)

# Start and end date route
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Start a session
    session = Session(engine)

    # Query min, avg, and max temps between the start and end dates
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Close the session
    session.close()

    # Convert the results to a dictionary
    temps = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temps)

#################################################
# Run the Flask App
#################################################
if __name__ == "__main__":
    # Open the app in the default web browser
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
