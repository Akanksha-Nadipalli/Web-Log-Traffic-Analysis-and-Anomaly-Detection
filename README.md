## 🌐 Web Log Traffic Analysis and Anomaly Detection

Access the deployed Streamlit application:  
🔗 https://web-traffic-anomaly-dashboard.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-green?style=for-the-badge&logo=scikitlearn)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-darkblue?style=for-the-badge&logo=plotly)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red?style=for-the-badge)
![Isolation Forest](https://img.shields.io/badge/Model-Isolation%20Forest-purple?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Anomaly%20Detection-brightgreen?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge)

---

## 📖 Overview

Web servers receive thousands of requests from different IP addresses.
Among them are:

✦ Normal users

✦ Bots

✦ Scrapers

✦ Suspicious automated traffic

Instead of checking requests one by one, this project models how each IP behaves over time and uses machine learning to detect abnormal behavior.

---

## 📊 Application Demo

### Landing Page
<img src="assets/web-log-dashboard-landing-page.jpeg" width="800">

### Log Upload Interface
<img src="assets/web-log-dashboard-upload-page.jpeg" width="800">

### Traffic Analysis Dashboard
<img src="assets/web-log-dashboard-analysis-dashboard.jpeg" width="800">

### Anomaly Report Download
<img src="assets/web-log-dashboard-report-download.jpeg" width="800">

---

## 🔍 Key Features

✦ Upload web server log files for automated analysis  

✦ Identify suspicious and anomalous IP behavior  

✦ Interactive dashboard for exploring traffic patterns  

✦ Visual insights into user activity and anomalies  

✦ Download anomaly detection results and reports  

---

## ⚙️ Workflow 
Raw Logs → Cleaning → Feature Engineering (per IP) → Isolation Forest → Visual Analysis

###  Log Parsing & Cleaning

Raw logs were converted into structured data with fields such as:

✦ IP address

✦ URL accessed

✦ Status code

✦ Request size

✦ Timestamp

✦ is_bot


###  Feature Engineering

We transform the dataset from:

1 row = 1 request to 1 row = behavior summary of 1 IP

For every IP, we compute:

| Feature                | Meaning                   |
| ---------------------- | ------------------------- |
| requests_per_ip        | Traffic volume            |
| unique_urls_per_ip     | Crawling diversity        |
| error_rate_per_ip      | Suspicious probing        |
| avg_size_per_ip        | Data access pattern       |
| bot_ratio_per_ip       | Bot-like behavior         |
| hour / is_night        | Time-based activity       |
| URL structure features | API/static/query behavior |


###  Anomaly Detection — Isolation Forest
Isolation Forest detects rare and unusual patterns without labels.

✦ Negative score → Anomalous IP

✦ Positive score → Normal IP  

---


## 📁 Project Structure

```
Web-Log-Traffic-Analysis-and-Anomaly-Detection/
│
├── assets/
|   ├── dashboard.gif         # Demo video of the application
│   ├── web-log-dashboard-landing-page.jpeg
│   ├── web-log-dashboard-upload-page.jpeg
│   ├── web-log-dashboard-analysis-dashboard.jpeg
│   └── web-log-dashboard-report-download.jpeg
│
├── data/                     
│   ├── cleaned_logs.csv     
│   ├── processed_features.csv
│   └── anomaly_scores.csv
│
├── models/                   # Trained ML models
│   ├── isolation_forest.pkl
│   └── scaler.pkl
│
├── plots/                    
│   ├── anomaly_score_distribution.jpeg
│   ├── bot_vs_human_requests.png
│   ├── activity_by_hour.jpeg 
│   └── error_rate_comparision.png
│
├── programfiles/             
│   ├── log_parsing_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── anomaly_model_training.ipynb
│   └── analysis_visualization.ipynb
│
├── app.py                    # Streamlit Dashboard application
├── README.md                 
├── requirements.txt          
└── abstract.pdf
```
---
## 🔮 Future Improvements

✦ Real-time log monitoring support  

✦ Integration with backend APIs  

✦ Support for larger datasets and scalable processing  

✦ Advanced anomaly detection models  

✦ User authentication and access control  
