# Device-price-classification-system
A Device Price Classification System using Spring Boot and Python leverages Spring Boot for backend services and Python for machine learning-based price prediction, classifying devices into price categories. It integrates data processing, model training, and REST APIs for real-time classification.
## project Structure
Device-price-classification-system/
│── databasefile/
│   ├── devices.db
│
│── python_model/
│   ├── app.py
│   ├── model.pkl
│   ├── train.py
│   ├── data/
│   │   ├── train.xlsx
│   │   ├── test.xlsx
│   ├── notebooks/
│       ├── data-processing.ipynb
│       
│── spring_boot_app/
│   ├── pom.xml
│   ├── src/
│   │   ├── main/
│   │       ├── java/
│   │       │   ├── com/example/deviceprice/
│   │       │   │   ├── DevicePricePredictionApplication.java
│   │       │   │   ├── controller/
│   │       │   │   │   ├── DeviceController.java
│   │       │   │   ├── model/
│   │       │   │   │   ├── Device.java
│   │       ├── resources/
│   │       │   ├── application.properties
│   │       │   ├── static/
│   │       │       ├── index.html

Summary:
• databasefile/: Contains devices.db (SQLite database for storage).
• python_model/: Python scripts for ML model training and deployment.
• app.py: Likely a Flask API to serve the model.
• train.py: Script to train the model.
• model.pkl: Saved machine learning model.
• data/: Contains train.xlsx and test.xlsx.
• notebooks/: Jupyter notebooks for data processing.
• spring_boot_app/: Java Spring Boot application.
• pom.xml: Maven configuration.
• src/main/java/com/example/deviceprice/: Main Java package.
• controller/: DeviceController.java (handles API requests).
• model/: Device.java (data model).
• resources/: application.properties (configuration) and static/index.html (frontend).
