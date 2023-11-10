#Day1
'''
streamlit hello
'''

#Day2  # streamlit run streamlit_app.py
'''
import streamlit as st

st.write('Hello world!')
'''

#Day3
'''
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
'''

#Day4

#Day5
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

st.write('Hello,*World!*:sunglasses:') #*斜体字，::表情

st.write(1234)

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

st.write(df)

st.write('Below is DataFrame:', df,'Above is a dataframe.')

df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)

c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
)

st.write(c)
