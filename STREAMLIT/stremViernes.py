import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
import psycopg2
import os 
import xlrd
import openpyxl
from funiconGraf import tipoenerW, tipoenerA, barPlot, lineal2Plot, tipoenerB, lineal2Plot2, linealTwh


with st.sidebar:
    choose = option_menu("Menu", ["Inicio", "Diccionarios"],
                         icons=['world', "world"],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "8!important", "background-color": "#202022"},
        "icon": {"color": "#00747C", "font-size": "15px"}, 
        "nav-link": {"font-size": "18px", "text-align": "down", "margin":"0px", "--hover-color": "#363333"},
        "nav-link-selected": {"background-color": "579DFF"},
    }
    )



if choose == "Inicio":
    sep1, sep2 = st.columns(2)
    
    with sep1:
        fig = tipoenerW()
        st.plotly_chart(fig)

    # with sep2:
    #     fig1 = tipoenerW(ener, "Energy_type", "Energy_consumption", "Year")
    #     st.plotly_chart(fig1)

    fig2 = tipoenerA()
    st.plotly_chart(fig2)
    fig3 = barPlot()
    st.plotly_chart(fig3)
    fig4 = lineal2Plot()
    st.plotly_chart(fig4)


    fig5 = tipoenerB()
    fig6 = linealTwh()
    fig7 = lineal2Plot2()
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)
    st.plotly_chart(fig7)