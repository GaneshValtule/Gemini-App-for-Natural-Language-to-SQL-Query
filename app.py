from dotenv import load_dotenv

# loading all the environment variables
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai


genai.configure(api_key=os.getenv("GENERATIVEAI_API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur =conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = """

You are an expert in converting English questions to SQL query!
The SQL database has the name sales and has the following columns - id sale_date customer_name product_name quantity price total
or example, Example 1 - What are the details of all sales for the product "Shirt"?, the SQL command will be something like this SELECT * FROM sales WHERE product_name = 'Shirt';
Example 2 – How many sales were made for each product? , the SQL command will be something like this SELECT product_name, COUNT(*) AS sale_count FROM sales GROUP BY product_name;
Example 3 – Give me the first 5 rows of the table, the SQL command will be something like this SELECT * FROM sales LIMIT 5;
also the sql code should not have ``` in beginning or end and sql word in the output
Also, if user greets you should also greet the user and if any question asked outside of the database it should return "Sorry, I don't understand, I am a bot for answering questions about retail data and can not answer your question."
"""

st.set_page_config(page_title="I can Retrieve ANy SQL query")
st.header("Gemini App to retrieve SQL Data")

question = st.text_input("Input",key = "input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"sales.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)