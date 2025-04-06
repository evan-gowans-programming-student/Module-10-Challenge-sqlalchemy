# Module 10: Climate Data Analysis with SQLAlchemy and Flask

## 📌 Overview

In this project, we performed a comprehensive climate data analysis for a vacation in **Honolulu, Hawaii**. Using **Python, SQLAlchemy, and Flask**, we explored historical climate data stored in an SQLite database, extracted actionable insights, and created a user-friendly API to share our findings.

The project is divided into two parts:
- **Part 1**: Climate Data Analysis
- **Part 2**: Flask API Development

---

## 🔧 Key Components

### 📊 Part 1: Climate Data Analysis

We used **SQLAlchemy ORM** to query and analyze the climate data in the `hawaii.sqlite` database. The dataset included two main tables:
- `measurement`: weather data
- `station`: weather station info

We used the following libraries:
- `Pandas`
- `Matplotlib`
- `datetime`

### 📌 Steps in Analysis

#### 🗄️ Database Setup

- Connected to SQLite using `create_engine`
- Reflected tables using SQLAlchemy Automap
- Established a session to interact with the database

#### 🌧️ Precipitation Analysis

- Queried 12 months of precipitation data prior to **2017-08-23**
- Created a **bar chart** to visualize daily precipitation
- Printed **summary statistics** using Pandas

#### 🛰️ Station Analysis

- Counted **9 total stations**
- Identified the **most active station**: `USC00519281`
- Retrieved **min, max, and average temperatures** for this station
- Queried temperature observations (**TOBS**) for the last year
- Plotted a **histogram** with 12 bins

---

### 🌐 Part 2: Flask API Development

We developed a **Flask API** to serve climate analysis results via HTTP routes. This allows users to fetch weather insights directly from their browsers or apps.

---

## 🔗 Available API Routes

| Route | Description |
|-------|-------------|
| `/` | Homepage listing all available routes |
| `/api/v1.0/precipitation` | JSON of precipitation data (last 12 months) |
| `/api/v1.0/stations` | JSON list of all station IDs |
| `/api/v1.0/tobs` | JSON list of TOBS for the most active station |
| `/api/v1.0/<start>` | Min/avg/max temps from start date onward |
| `/api/v1.0/<start>/<end>` | Min/avg/max temps for the given date range |

---

## 🧠 Development Highlights

- Used **Flask** to define API endpoints and serve JSON responses
- Managed database queries with **SQLAlchemy ORM**
- Returned clean, structured **JSON** for easy integration

---

## 📁 File Structure

```bash
/sqlalchemy-challenge
├── Resources/
│   └── hawaii.sqlite            # SQLite DB with climate data
├── app.py                       # Flask API script
├── climate_starter.ipynb        # Data analysis in Jupyter
├── README.md                    # This project documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/sqlalchemy-challenge.git
cd sqlalchemy-challenge
```

### 2. Install Dependencies

Make sure you have these Python packages:

- Flask  
- SQLAlchemy  
- Pandas  
- Matplotlib

Install them with:

```bash
pip install flask sqlalchemy pandas matplotlib
```

### 3. Run the Flask App

```bash
python app.py
```

---

## 🌐 Access the API

Once the server is running, open your browser and go to:

```
http://127.0.0.1:5000/
```

### Test Routes

- **Precipitation**  
  `http://127.0.0.1:5000/api/v1.0/precipitation`

- **Stations**  
  `http://127.0.0.1:5000/api/v1.0/stations`

- **Temperature Observations**  
  `http://127.0.0.1:5000/api/v1.0/tobs`

- **Start Date Query**  
  `http://127.0.0.1:5000/api/v1.0/2017-08-01`

- **Start and End Date Query**  
  `http://127.0.0.1:5000/api/v1.0/2017-08-01/2017-08-15`

---

## 🎓 Key Learnings

- ✅ **SQLAlchemy ORM**: Automapped and queried database tables like Python objects  
- ✅ **Data Analysis**: Used `Pandas`, `Matplotlib`, and `datetime` to explore and visualize trends  
- ✅ **RESTful API Design**: Created dynamic, user-friendly endpoints  
- ✅ **JSON Responses**: Served structured data to API consumers in standard formats

---

*This project is part of the Data Analytics Bootcamp curriculum and demonstrates foundational skills in data engineering and web-based data sharing.*
