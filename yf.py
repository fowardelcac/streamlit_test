# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:37:00 2023

@author: USUARIO
"""

import pandas as pd
import yfinance as yf
import streamlit as st

df = yf.download("TSLA")

st.header('''
            TESLA STOCK
          ''')
st.write("Tesla adj close: ", df['Adj Close'])

st.line_chart(df['Adj Close'])
