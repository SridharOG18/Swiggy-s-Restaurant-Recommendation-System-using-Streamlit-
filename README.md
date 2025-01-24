# Swiggy-s-Restaurant-Recommendation-System-using-Streamlit-

# **Swiggy Restaurant Analysis and Recommendation System**

## **Project Overview**
This project, titled **"Swiggy Restaurant Analysis and Recommendation System,"** combines data cleaning, preprocessing, and visualization with an interactive web application to explore restaurant data effectively. Inspired by the design of Swiggy's platform, the application provides a user-friendly interface to filter restaurants based on various criteria and gain insights into the restaurant industry.

## **Industry Domain**
- **Food Delivery & Hospitality**: This project is built to analyze restaurant data, offering features that improve decision-making for both users and business owners in the food delivery space.

## **Key Skills**
- **Python Scripting**
- **Data Preprocessing**
- **Machine Learning Models**
- **Streamlit Web App Development**

## **Technologies Used**
- **Python 3.9+**
- **Streamlit**
- **scikit-learn**
- **pandas**
- **NumPy**

## **Application Features**

### **1. Data Cleaning & Preprocessing**
- Removed unnecessary columns like `lic_no`, `link`, `address`, and `menu`.
- Converted categorical columns into numerical representations using label encoding.
- Standardized `rating_count` and removed special symbols (e.g., ₹ from cost).
- Applied feature scaling using `StandardScaler`.

### **2. Clustering & Recommendations**
- Implemented MiniBatch KMeans for clustering restaurants based on encoded data.
- Enabled grouping of restaurants into clusters for efficient exploration.

### **3. Interactive Web App with Streamlit**
- A visually appealing application inspired by Swiggy's design.
- Features include:
  - **Filter Options**: City, Cuisine, Price Range, and Ratings in a horizontal layout.
  - **Detailed Restaurant View**: Displays restaurant information with styled cards.
  - **Dynamic Clustering**: Shows clusters of restaurants for better decision-making.

### **4. User-Friendly Aesthetic**
The interface is designed with a focus on simplicity, responsiveness, and aesthetics to ensure a seamless experience for users.

---

## **Packages and Libraries Used**
- **Data Processing**: `pandas`, `numpy`
- **Machine Learning**: `scikit-learn`
- **Web App Development**: `streamlit`, `streamlit_option_menu`
- **Visualization**: `matplotlib`, `seaborn`

---

## **Screenshots**

### **Application Layout**
![Project Screenshot](https://github.com/SridharOG18/Swiggy_Project/blob/main/Screenshots/Swiggy_App.png?raw=true)

---

## **Author**

**Sridhar**


