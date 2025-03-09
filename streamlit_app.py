# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.40?")
st.divider()

with st.sidebar:
    st.logo(path_cda + '\\logo.png', size='large')
    st.empty()
#
#

def page1():
    st.header(':one: Introducing st.pills to create a single- or multi-select group of pill-buttons')

    st.code('''
    language = st.pills('Choose language:', options=['English', 'French', 'German', 'Spanish'])
    if language: st.write(f'You have chosen: {language}')
    ''')

    choice = st.pills('Choose language:', options=['English', 'French', 'German', 'Spanish'])
    if choice: st.write(f'You have chosen: {choice}')

    st.code('''
    language = st.pills('Choose language:', options=['English', 'French', 'German', 'Spanish'], selection_mode='multi')
    if language: st.write(f'You have chosen: {language}')
    ''')

    choice = st.pills('Choose language:', options=['English', 'French', 'German', 'Spanish'], selection_mode='multi', key='t')
    if choice: st.write(f'You have chosen: {choice}')

    st.code('''
    choice = st.pills('Choose action:', options=['download', 'upload', 'delete'],
                      format_func=lambda option: {'download': ":material/download:",
                                                  'upload': ":material/upload:",
                                                  'delete': ":material/delete:"}.get(option, option))
    if choice: st.write(f'You have chosen: {choice}')
    ''')

    choice = st.pills('Choose action:', options=['download', 'upload', 'delete'],
                      format_func=lambda option: {'download': ":material/download:",
                                                  'upload': ":material/upload:",
                                                  'delete': ":material/delete:"}.get(option, option))
    if choice: st.write(f'You have chosen: {choice}')

def page2():
    st.header(':two: Introducing st.segmented_control to create a segmented button or button group')

    st.code('''
    language = st.segmented_control('Choose language:', options=['English', 'French', 'German', 'Spanish'])
    if language: st.write(f'You have chosen: {language}')
    ''')

    choice = st.segmented_control('Choose language:', options=['English', 'French', 'German', 'Spanish'])
    if choice: st.write(f'You have chosen: {choice}')

    st.code('''
    language = st.segmented_control('Choose language:', options=['English', 'French', 'German', 'Spanish'], selection_mode='multi')
    if language: st.write(f'You have chosen: {language}')
    ''')

    choice = st.segmented_control('Choose language:', options=['English', 'French', 'German', 'Spanish'], selection_mode='multi', key='t')
    if choice: st.write(f'You have chosen: {choice}')

    st.code('''
    choice = st.segmented_control('Choose action:', options=['download', 'upload', 'delete'],
                      format_func=lambda option: {'download': ":material/download:",
                                                  'upload': ":material/upload:",
                                                  'delete': ":material/delete:"}.get(option, option))
    if choice: st.write(f'You have chosen: {choice}')
    ''')

    choice = st.segmented_control('Choose action:', options=['download', 'upload', 'delete'],
                      format_func=lambda option: {'download': ":material/download:",
                                                  'upload': ":material/upload:",
                                                  'delete': ":material/delete:"}.get(option, option))
    if choice: st.write(f'You have chosen: {choice}')

def page3():
    st.header(':three: Announcing the general availability of st.audio_input, a widget to let users record sound with their microphones')

    st.code('''
    st.audio_input('Record something!')
''')
    st.audio_input('Record something!')

def pagem():
    st.header(':four: Markdown renders a limited set of typographical symbols (arrows and comparators)')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.39')
    cols[1].subheader('Streamlit 1.40')


    with cols[0]:
        st.code('''
            st.markdown('This is a list of symbols: <- -> <-> -- >= <= ~=')
        ''')
        st.text('This is a list of symbols: <- -> <-> -- >= <= ~=')


    with cols[1]:
        st.code('''
            st.markdown('This is a list of symbols: <- -> <-> -- >= <= ~=')
        ''')
        st.markdown('This is a list of symbols: <- -> <-> -- >= <= ~=')

    st.header(":five: st.date_input infers the first day of the week from the user's locale")
    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.39')
    cols[1].subheader('Streamlit 1.40')
    cols[0].code(''' 
    .''')
    cols[1].code('''st.date_input('Select date:')''')
    cols[1].date_input('Select date:')

    st.header(':six: You can set use_container_width for st.image. use_column_width is deprecated')
    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.39')
    cols[1].subheader('Streamlit 1.40')
    cols[0].code('''st.image('image.png', use_column_width=True)''')
    cols[0].image(path_cda + '\\background.png', use_container_width=True)
    cols[1].code('''st.image('image.png', use_container_width=True)''')
    cols[1].image(path_cda + '\\background.png', use_container_width=True)

def pageX():
    st.header(':one: ')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.38')
    cols[1].subheader('Streamlit 1.39')


    with cols[0]:
        st.code('''

        ''')


    with cols[1]:
        st.code('''

        ''')

pg = st.navigation([st.Page(page1, title='st.pills'),
                    st.Page(page2, title='st.segmented_control'),
                    st.Page(page3, title='st.audio_input'),
                    st.Page(pagem, title='Miscellaneous')])
pg.run()