import streamlit as st
from Back_End import table_crete, update_date, Total_Expense, Show_data, Delete_data
import sqlite3
import pandas as pd

st.title("Monthly Expense Calculator")

table_crete()

Option_2 = ['Add new data', 'update the data', 'Total expense spend', 'Show data', 'Delete the data']

option_3 = {'Vegetables', 'Food', 'Grocery', 'Movie', 'Shopping', 'others'}

option = st.selectbox("Select the option", Option_2)

if option == "Add new data":
    date = st.date_input("Enter the date")
    Exp_type = st.radio("Mention the type", ('Personal', 'Common'))
    category = st.selectbox("select your category of expenses",
                            option_3)
    if category == "others":
        category = st.text_input("Enter the specific category")
    amount = st.number_input("Enter the Amount")
    remarks = st.text_input("Remarks")
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "INSERT into Exp (Date, Type, Category, Amount, Remarks) values (?, ?, ?, ?, ?)"
        # noinspection PyUnboundLocalVariable
        data = (date, Exp_type, category, amount, remarks)
        cursor.execute(sql, data)
        con.commit()
        con.close()
        st.success("New data added successfully")


elif option == "update the data":
    update_date()

elif option == "Total expense spend":
    Total_Expense()

elif option == "Show data":
    Show_data()

elif option == "Delete the data":
    Delete_data()
