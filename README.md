# Disease-Prediction-Project

# 🩺 Multi-Disease Prediction System

The **Multi-Disease Prediction System** is a machine learning-powered web application that predicts the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson's Disease** based on user-provided health data. Built using **Streamlit**, this project provides a user-friendly interface and leverages pre-trained models for accurate and efficient health predictions.

---

## 🚀 Features
- **Multiple Disease Prediction:** Supports predictions for Diabetes, Heart Disease, and Parkinson's Disease.
- **Interactive Web Interface:** Built with **Streamlit** for ease of use.
- **Real-Time Predictions:** Instant health risk assessment based on input data.
- **Pre-trained ML Models:** Models trained using real-world medical datasets.
- **Fast & Lightweight:** Optimized for quick execution and smooth performance.

---

## 🖥️ Demo
To run the application locally:

```bash
streamlit run app.py
```

_Add a GIF or screenshot of your app in action here._

---

## 📂 Project Structure

```
Multi_Disease_Prediction/
│
├── datasets/               # Contains datasets for Diabetes, Heart Disease, and Parkinson's
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
│
├── models/                 # Pre-trained ML models saved in .sav format
│   ├── diabetes_model.sav
│   ├── heart_model.sav
│   └── parkinsons_model.sav
│
├── notebooks/              # Jupyter Notebooks for data analysis & model training
│   ├── Diabetes_Prediction.ipynb
│   ├── Heart_Disease_Prediction.ipynb
│   └── Parkinsons_Prediction.ipynb
│
├── app.py                  # Streamlit application code
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation (this file)
```

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** for creating the interactive web app
- **Scikit-learn** for machine learning models
- **Pandas** & **NumPy** for data processing
- **Matplotlib** & **Seaborn** for data visualization
- **Pickle** for model serialization

---

## 📊 How It Works

1. **Data Processing:**
   - Load datasets for Diabetes, Heart Disease, and Parkinson's.
   - Clean, preprocess, and normalize the data for model training.

2. **Model Training:**
   - Various machine learning algorithms (Logistic Regression, Random Forest, etc.) are tested.
   - The best-performing models are saved as `.sav` files using `pickle`.

3. **Web Application (Streamlit):**
   - Users input their health parameters into the app.
   - The selected pre-trained model predicts the disease likelihood.
   - Results are displayed in real time.

---

## 📥 Installation Guide

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Multi_Disease_Prediction.git
   cd Multi_Disease_Prediction
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

---

## 📸 Screenshots
![Screenshot (45)](https://github.com/user-attachments/assets/d9aa24ee-3acb-4218-8250-9ca44665ff9c)
![Screenshot (47)](https://github.com/user-attachments/assets/199e8db8-f148-4ac2-b966-e52bd79e5de7)
![Screenshot (46)](https://github.com/user-attachments/assets/71565369-630a-41ea-b082-29dad03ba054)

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repository.**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/Multi_Disease_Prediction.git
   ```
3. **Create a new branch:**
   ```bash
   git checkout -b feature-name
   ```
4. **Make your changes and commit:**
   ```bash
   git commit -m "Describe your changes"
   ```
5. **Push to your branch:**
   ```bash
   git push origin feature-name
   ```
6. **Open a Pull Request.**

---

## 🙌 Acknowledgements

- Datasets sourced from reputable health data repositories.
- Inspired by modern AI applications in healthcare.

---

