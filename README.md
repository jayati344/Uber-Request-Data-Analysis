# Uber Request Data Analysis 🚕📊

This project aims to analyze Uber ride request data to identify operational inefficiencies, particularly during peak hours. Using Python and data visualization techniques, we explore patterns in ride status, time-based demand fluctuations, and pickup point dynamics.

---

## 📌 Problem Statement

Uber observed a high rate of trip cancellations and unfulfilled requests, especially during certain hours of the day. This analysis investigates:
- When and where most ride requests fail
- Whether cancellations are concentrated at specific locations or times
- How demand patterns can guide Uber’s resource allocation

---

## 📁 Dataset Overview

The dataset contains details of ride requests, including:
- Request timestamp
- Drop timestamp
- Pickup point (City or Airport)
- Ride status (Completed, Cancelled, No Cars Available)

*Note: The dataset used was provided as a CSV file named `Uber Request Data.csv`.*

---

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🧠 Key Tasks Performed

- Data cleaning and timestamp conversion
- Extraction of hour and day from request times
- Creation of custom time slots: Morning Rush, Evening Rush, etc.
- Visualization of request status vs. time of day and pickup location
- Identification of failure patterns (e.g., high cancellation rates at airport during morning rush)

---

## 📊 Visual Insights

- Count plots showing trip statuses across different hours and days
- Comparison of city vs. airport pickups in peak slots
- Analysis of completed vs. failed trips during specific time slots

---

## 📈 Key Findings

- **Morning Rush (5–10 AM)** saw a high number of cancellations, especially from the **Airport**.
- **Evening Rush (5–10 PM)** faced frequent **"No Cars Available"** issues from the **City**.
- Imbalance in cab supply between Airport and City during peak hours is evident.

---

## ✅ Conclusion

Improving resource allocation based on time and location-specific demand could significantly reduce unfulfilled requests. This analysis helps Uber recognize peak problem zones and times for better fleet management.

---

## 📎 How to Run

1. Download the dataset (`Uber Request Data.csv`)
2. Run the `.py` or `.ipynb` file using Jupyter Notebook or any Python IDE
3. Make sure required libraries are installed (`pandas`, `matplotlib`, `seaborn`, etc.)

---




