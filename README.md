# 🏦 Bank Loan Prediction System

## 📌 Overview

This project uses Machine Learning to predict whether a loan application will be **approved or rejected** based on customer details like income, credit history, and loan amount.

💡 Beginner-friendly note:
The model works like a bank officer who decides *“loan dena chahiye ya nahi”* but faster and based on data.

---

## 🎯 Objective

* Automate loan approval prediction
* Reduce human effort
* Improve decision accuracy

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Jupyter Notebook

---

## ⚙️ Project Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. ROC Curve Analysis
8. Model Saving

---

## ✨ Features

- 📊 **Exploratory Data Analysis (EDA)** — Visualizes income distribution, outliers, and loan approval rates
- 🔍 **Missing Value Handling** — Detects and manages null values in the dataset
- 🧹 **Data Preprocessing** — Encodes categorical variables using Label Encoding
- 📈 **Correlation Heatmap** — Identifies which features influence loan approval the most
- 🤖 **Dual Model Comparison** — Trains both Decision Tree and Logistic Regression models
- 📉 **ROC Curve Visualization** — Compares model performance graphically
- 💾 **Model Export** — Saves the trained model using Pickle for future deployment
- 📋 **Classification Report** — Provides Precision, Recall, and F1-Score metrics
  
---

## 🤖 Models Used

* **Logistic Regression** --> A simple yet powerful algorithm that calculates the *probability* of loan approval as a value between 0 and 1.
* **Decision Tree** --> The tree is **pruned** (limited in size) to prevent overfitting — a common problem where a model memorizes training data but performs poorly on new data.

👉 Both models are trained and compared to find the best one.

---

## 📊 Model Evaluation

We evaluate models using:

| Model | Accuracy | ROC-AUC Score |
|-------|----------|---------------|
| Decision Tree | `92%`  | `0.92` |
| Logistic Regression | `0.80%` | `0.74` |

---

## 📉 ROC Curve

📌 Add screenshot here:

```
<img width="1920" height="1440" alt="ROC Curve" src="https://github.com/user-attachments/assets/1de0f14a-9148-4ad4-96d3-3315b5287995" />


---

## 🖼️ Screenshots

1. Dataset Preview

```
<img width="875" height="516" alt="Dataset 2026-04-10 003908" src="https://github.com/user-attachments/assets/35f63cbd-e1db-4eb9-b15a-9ca62efa461c" />

```

2. EDA Graph (Income / Distribution)

```
<img width="1920" height="1440" alt="Histogram_Income" src="https://github.com/user-attachments/assets/35ad85c0-7e7c-4e87-9004-08c1f565cdf8" />
```

3. Correlation Heatmap

```
<img width="3600" height="1800" alt="correlation" src="https://github.com/user-attachments/assets/b5b32df1-6808-42d3-8372-be071f824780" />
```

4. Confusion Matrix

```
<img width="1342" height="417" alt="Confusion_Matrix 2026-04-10 005015" src="https://github.com/user-attachments/assets/a5f4784f-505b-4c65-b6cc-f63bb7022c46" />
```

5. ROC Curve

```
<img width="2400" height="1800" alt="ROC Curve Comparison" src="https://github.com/user-attachments/assets/0795784a-d99a-48c3-b1ad-5432c3169cf0" />
```

---

## 📁 Project Structure

```
bank-loan-prediction/
│
├── notebook/
│   └── model.ipynb
│
├── model/
│   └── model.pkl
│
├── data/
│   └── dataset.csv
│
├── screenshots/
│
├── app.py 
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Project

```bash
git clone https://github.com/your-username/bank-loan-prediction.git
cd bank-loan-prediction
pip install -r requirements.txt
jupyter notebook
```

---

## 🌐 Live Project

👉 Add your deployed link here:

```
https://your-live-project-link.com

---

## 🔗 Important Links

* GitHub Repository:

```
https://github.com/tushantac2003-prog/Bank-Loan-Prediction
---

## 💾 Model Saving

The trained model is saved using:

```python
import pickle
pickle.dump(bl, open(r"C:\Users\tusha\Downloads\build.pkl",'wb')) 
```

## 📈 Results

* Model successfully predicts loan approval
* ROC-AUC score shows good performance
* Decision Tree 

---

## 🔮 Future Improvements

* Add Random Forest / XGBoost
* Improve accuracy

---

## 👤 Author

Tushant Chaudhari

* GitHub: https://github.com/tushantac2003-prog
* LinkedIn:https://www.linkedin.com/in/tushant-chaudhari-a62b10298

---

⭐ If you like this project, give it a star!
