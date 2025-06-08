# 🏥 Healthcare Appointment No-Show Prediction

This project predicts whether a patient will miss their medical appointment using machine learning and provides actionable insights through a Power BI dashboard.

## 📌 Objective
To predict patient no-shows and help optimize hospital scheduling by analyzing patterns such as age, reminders, day of the week, and more.

---

## 🛠️ Tools & Technologies

-  Python (Pandas, Scikit-learn)
- 📊 Power BI
- 📓 Jupyter Notebook
- 📁 Excel

---

## 📂 Project Structure

```bash
📁 Healthcare_No_Show_Prediction/
├── 📊 No_Show_Dashboard.pbix                       
├── 📓 Python_notebook.ipynb 
├── 📁 PROJECT .xlsx          
├── 📄 Healthcare_No_Show_Prediction_Report.pdf 
├── 📄 README.md                                 
```
---

## 📈 Data Overview

- **Source**: Appointment dataset (CSV)
- **Target Variable**: `No_show` (Yes = patient missed, No = patient came)
- **Key Features**: Age, Gender, SMS_received, Scholarship, Handcap, WaitingDays

---

## 🧹 Data Preprocessing

- Renamed and cleaned columns
- Converted `ScheduledDay` and `AppointmentDay` to datetime
- Calculated `WaitingDays` (appointment delay)
- Removed negative intervals
- Encoded categorical values (`Gender`, `No_show`)

---

## 🤖 Machine Learning Model

- **Model Used**: Decision Tree Classifier (`max_depth=5`)
- **Train/Test Split**: 80/20
- **Evaluation**: Classification Report & Accuracy Score
- **Output**: Python_notebook.ipynb

---

## 📊 Power BI Dashboard

Key visual insights:
- No-shows by **SMS reminders**
- No-shows across **days of the week**
- Impact of **age**, **gender**, and **neighbourhood**
- Slicers for custom filtering

- <a href="https://github.com/yashh1910/Healthcare-Appointment-No-Show-Prediction/blob/main/No_Show_Dashboard.pbix"> No_Show_Dashboard</a>

---

## 🔍 Key Insights

- Patients **not receiving SMS** are more likely to miss appointments
- **Wednesdays and Fridays** had higher no-show rates
- Certain **neighbourhoods** showed recurring high no-show patterns

---

## ✅ Optimization Recommendations

- Send **SMS reminders** to all patients by default
- Avoid scheduling critical appointments on **high no-show days**
- Implement **location-specific outreach** strategies

---

## 📦 Deliverables

- ✅ Cleaned dataset in Excel
- ✅ Trained machine learning model
- ✅ Power BI interactive dashboard
- ✅ PDF project report 

---

## 📧 Contact

**Author:** Yash Patel  
**Email:** yashp19102001@gmail.com





