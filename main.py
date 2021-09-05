import streamlit as st
from heatmaps import heatmaps
from time_series import time_series
import pandas as pd
st.write('店舗画面')
file = st.file_uploader("ファイルアップロード", type='csv')

if file is not None:
    file = pd.read_csv(file)
    option = st.selectbox('サービスを選択してください',('-', 'ヒートマップ・円グラフ', '時系列可視化'))
    if option == 'ヒートマップ・円グラフ':
        heatmaps(file)
    if option == '時系列可視化':
        time_series(file)
        