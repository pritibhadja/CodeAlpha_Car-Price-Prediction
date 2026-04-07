# CarVal — AI-Powered Car Price Predictor

CarVal is a machine learning web application designed to estimate the resale value of used cars based on various features such as year of manufacture, present price, distance driven, fuel type, transmission, and ownership history. 

The application uses a **Random Forest Regressor** model trained on Indian car market data to provide accurate estimations through a clean, modern web interface.

## 🚀 Features

- **Instant Estimation:** Get car price predictions in seconds.
- **Interactive UI:** A modern, dark-themed responsive web interface built with Custom CSS and Google Fonts (Syne & DM Sans).
- **Comprehensive Inputs:** Factors in multiple variables including:
    - Vehicle Age (Year)
    - Showroom Price (Present Price)
    - Kilometers Driven
    - Fuel Type (Petrol/Diesel/CNG)
    - Transmission (Manual/Automatic)
    - Seller Type (Dealer/Individual)
    - Previous Owners

---

## 🧠 Machine Learning Model

The core of this project is a regression-based machine learning pipeline:

- **Algorithm:** `RandomForestRegressor` (Ensemble Learning).
- **Pre-processing:** - Categorical variables (Fuel Type, Seller Type, Transmission) are converted using **One-Hot Encoding**.
    - Feature selection and alignment are managed via `columns.pkl` to ensure the web app matches the training data structure.
- **Algorithm used**: Linear Regression (or based on your notebook)
- **Trained on dataset**: `car_data.csv`
- **Model file**: `model.pkl`
- **Feature encoding handled using**: `columns.pkl`

---

## 🛠️ Technologies Used

### 💻 Frontend
- HTML5  
- CSS3  
- JavaScript  

### ⚙️ Backend
- Python  
- Flask  

### 🗄️ Machine Learning
- Pandas  
- NumPy  
- Scikit-learn  

### 🧰 Tools
- Jupyter Notebook (`model.ipynb`)  
- Pickle (for model saving)  
- VS Code

## 📁 Project Structure

```text
├── app.py              # Flask application backend
├── model.pkl           # Serialized Random Forest model
├── columns.pkl         # Feature column structure for consistency
├── car_data.csv        # Dataset used for training
├── model.ipynb         # Jupyter notebook with training logic & evaluation
├── static/
│   ├── style.css       # Custom modern dark-theme styling
│   └── script.js       # UI logic and loading states
└── templates/
    ├── index.html      # Main input form (User Interface)
    └── result.html     # Prediction result display page

---

## 📂 Project Structure

