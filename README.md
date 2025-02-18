# Device Price Classification System

## Overview
The **Device Price Classification System** is a machine learning-based application that predicts device prices. It consists of a **Python-based ML model** and a **Spring Boot REST API** for deployment.

---

## Project Structure
```
Device-price-classification-system/
│── databasefile/
│   ├── devices.db              # SQLite database file
│
│── python_model/               # Machine Learning Model
│   ├── app.py                  # Flask API for ML model
│   ├── train.py                # Script to train the ML model
│   ├── model.pkl               # Trained model file
│   ├── data/                   # Dataset directory
│   │   ├── train.xlsx          # Training dataset
│   │   ├── test.xlsx           # Testing dataset
│   ├── notebooks/              # Jupyter Notebooks for EDA and preprocessing
│       ├── data-processing.ipynb  # Data processing notebook
│      
│
│── spring_boot_app/            # Backend API (Spring Boot)
│   ├── pom.xml                 # Maven configuration file
│   ├── src/main/java/com/example/deviceprice/
│   │   ├── DevicePricePredictionApplication.java  # Main Spring Boot Application
│   │   ├── controller/
│   │   │   ├── DeviceController.java   # REST API Controller
│   │   ├── model/
│   │   │   ├── Device.java             # Data Model
│   ├── src/main/resources/
│   │   ├── application.properties      # Configuration file
│   │   ├── static/
│   │       ├── index.html              # Frontend UI
```

---

## Setup Guide
### 1. Machine Learning Model (Python)
#### Prerequisites:
- Python 3.x
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
#### Steps:
- Train the model:
  ```sh
  python python_model/train.py
  ```
- Start the Flask API:
  ```sh
  python python_model/app.py
  ```

---

### 2. Spring Boot Backend
#### Prerequisites:
- Java 11+
- Maven
#### Steps:
- Navigate to `spring_boot_app/`
- Build and run the Spring Boot application:
  ```sh
  mvn spring-boot:run
  ```

---

## Usage
- **ML Model**: Predicts the price category of a device.
- **REST API**: Serves model predictions and interacts with a database.
- **Database**: Stores device data using SQLite.

---
