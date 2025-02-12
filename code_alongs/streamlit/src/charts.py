from read_data import read_data
import duckdb
import streamlit as st

def approved_by_area_bar():
    df = read_data()

    df = duckdb.query(
        """SELECT 
        utbildningsområde, count(*) AS Beviljade
        FROM df
        where beslut = 'Beviljad'
        group by utbildningsområde
        order by Beviljade desc
        """
    ).df()

    st.bar_chart(df,x="Utbildningsområde", y= "Beviljade")
