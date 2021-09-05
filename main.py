import streamlit as st
from heatmaps import heatmaps
st.write('店舗画面')
file = st.file_uploader("ファイルアップロード", type='csv')
if file is not None:
    option = st.selectbox('サービスを選択してください',('-', 'ヒートマップ・円グラフ', '時系列可視化'))
    if option == 'ヒートマップ・円グラフ':
        heatmaps(file)