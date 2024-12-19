import streamlit as st
from json import loads
from pandas import read_csv
import csv


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    #text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">clique aqui</a>'

st.title('Visualizador de arquivos')

file = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['txt', 'json', 'jpg', 'png', 'csv', 'py', 'mp3', 'mp4']
)

if file:
    if file.type == 'text/plain':
        st.text(file.read().decode())
    elif file.type == 'application/json':
        st.json(loads(file.read()))
    elif file.type == 'image':
        st.image(file)
    elif file.type == 'text/csv':

        df = read_csv(file,sep=",")
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        #df = df.to_html(escape=False)
        #    st.write(df, unsafe_allow_html=True)
        #st.dataframe(df)
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

        
    elif file.type == 'text/x-python':
        st.code(file.read().decode(), language='python')
    elif file.type == 'audio/mpeg':
        st.audio(file)
    elif file.type == 'video/mp4':
        st.video(file)
    else:
        st.error('Formato de arquivo não suportado!')
else:
    st.warning('Ainda não tenho arquivo!')