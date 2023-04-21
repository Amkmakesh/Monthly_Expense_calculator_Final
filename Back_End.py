import sqlite3
import streamlit as st
import pandas as pd


def table_crete():
    con = sqlite3.Connection("Exp_web.dp")

    cursor = con.cursor()

    Table = """CREATE TABLE if not exists Exp
                (ID INTEGER NOT NULL PRIMARY KEY,
                Date DATE,
                Type VARCHAR(100),
                Category VARCHAR(100),
                Amount FLOAT, 
                Remarks VARCHAR(100));"""

    cursor.execute(Table)
    con.close()

def update_date():
    id = st.number_input("Enter the id to update")
    date = st.date_input("Enter the date")
    Exp_type = st.radio("Mention the type", ('Personal', 'Common'))
    category = st.selectbox("select your category of expenses",
                            ('Vegetables', 'Food', 'Grocery', 'Movie', 'Shopping', 'others'))
    if category == "others":
        category = st.text_input("Enter the specific category")
    amount = st.number_input("Enter the Amount")
    remarks = st.text_input("Remarks")
    Note = st.write("All fields are required**")
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "Update Exp set Date=?, Type=?, Category=?, Amount=?, Remarks=? Where id=?"
        data_update = (date, Exp_type, category, amount, remarks, id)
        cursor.execute(sql, data_update)
        con.commit()
        con.close()
        st.success("Data updated successfully")


def Total_Expense():
    Start_date = st.date_input("Select the start day to calculate expenses")
    End_date = st.date_input("Select the End day to calculate expenses")
    Exp_type = str(st.selectbox("Mention the type", ('Personal', 'Common')))
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "SELECT total(Amount) FROM Exp WHERE date BETWEEN ? AND ? AND Type = ?"
        cursor.execute(sql, (Start_date, End_date, Exp_type))
        con.commit()
        st.write("The total amount spend:")
        st.write(cursor.fetchone()[0])
        con.close()
def Show_data():
    Start_date = st.date_input("Select the start day to show the expenses")
    End_date = st.date_input("Select the End day to show the expenses")
    Exp_type = str(st.selectbox("Mention the type", ('Personal', 'Common')))
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "select ID, Date, Type, Category, Amount, Remarks from Exp  WHERE date BETWEEN ? AND ? AND Type = ?"
        df = pd.read_sql_query(sql, con, params=(Start_date, End_date, Exp_type))
        df = pd.DataFrame(df).set_index("ID")
        st.table(df)
        con.close()

def Delete_data():
    con = sqlite3.Connection("Exp_web.dp")
    cursor = con.cursor()
    sql = "select ID, Date, Type, Category, Amount, Remarks from Exp"
    df = pd.read_sql_query(sql, con)
    df = pd.DataFrame(df).set_index("ID")
    st.table(df)
    con.close()
    to_delete = st.number_input("Enter the id to delete.")
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "delete from Exp where id=?"
        data = (to_delete,)
        cursor.execute(sql, data)
        con.commit()
        con.close()
        st.success("Data deleted successfully")
