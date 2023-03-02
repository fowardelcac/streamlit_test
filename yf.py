# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:37:00 2023

@author: USUARIO
"""

import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime


df = yf.download("TSLA")

st.header('''
            $TSLA
          ''')
st.write("Tesla adj close: ", df['Adj Close'])

st.line_chart(df['Adj Close'])

df.reset_index(inplace=True)


inicio_str = df['Date'].loc[0]
fin_str = df['Date'].loc[df.index[-1]]

inicio = datetime.strptime(str(inicio_str), '%Y-%m-%d %H:%M:%S')
fin = datetime.strptime(str(fin_str), '%Y-%m-%d %H:%M:%S')

#inicio_seleccionado, fin_seleccionado = st.slider(
 #   "Seleccione rango de fecha.", inicio, fin, (inicio, fin)
#) '''

inicio_seleccionado, fin_seleccionado = st.sidebar.slider(
    "Seleccione rango de fecha.", inicio, fin, (inicio, fin)
)


df.set_index('Date', inplace=True)
df_cop = df.loc[(df.index >= inicio_seleccionado) & (df.index <= fin_seleccionado)]


#st.write("Grafico de acuerdo al delizador: ")
option = st.selectbox(
     'que desea ver?',
     ('Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'))

if option != 'Volume':
    st.line_chart(df_cop[option])
else:
    st.bar_chart(df_cop[option])


options = st.multiselect(
     'What are your favorite colors',
     ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'],
     ['Adj Close'])

if options != 'Volume':
    st.line_chart(df[options])
else:
    st.bar_chart(df['Volume'] )
    options.remove('Volume')
    st.line_chart(df[options])
