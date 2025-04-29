# 🧠 Gemini App: Natural Language to SQL Converter for Sales Data

**Tech Stack:** Python · Streamlit · SQLite · Google Generative AI API

---

## 🚀 Project Overview
This project is an interactive **Streamlit application** that integrates with **Google Gemini** to convert **natural language queries** into executable **SQL commands** on structured sales data.  
It empowers users to analyze sales performance, revenue trends, and customer behavior without writing any SQL code.

---

## 📦 Dataset Structure
The sales dataset is stored in a **SQLite** database with the following schema:

| Column         | Description                    |
|----------------|--------------------------------|
| `id`           | Unique identifier for the sale |
| `sale_date`    | Date of the sale               |
| `customer_name`| Name of the customer           |
| `product_name` | Name of the product sold       |
| `quantity`     | Quantity sold                  |
| `price`        | Price per unit                 |
| `total`        | Total sale amount              |

---

## ⚙️ Features

- 🔍 **Natural Language to SQL**: Converts user input like _"Show total sales by product"_ into valid SQL.
- 🗃 **SQLite Backend**: Uses SQLite to store and query the dataset efficiently.
- 📊 **Dynamic Data Analysis**: Supports **filtering**, **grouping**, and **aggregation** of sales data.
- 🧠 **Google Gemini Integration**: Leverages Generative AI to translate natural language into accurate SQL queries.
- 🧾 **Error Handling**: Provides informative responses for queries beyond the dataset scope.
- 📈 **Real-Time Output**: Displays query results in an intuitive, interactive table within the Streamlit app.

---

## 💡 Use Cases

- Filter products by name or category  
- Analyze sales performance over time  
- Identify top-selling products or high-spending customers

---

## 🖥️ App Demo
> *(Add screenshots or screen recording if available)*

---

Would you like me to include sections for installation steps or examples of natural language queries too?
