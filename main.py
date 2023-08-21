import streamlit as st
import numpy as np
import pandas as pd

def main():
    # サンプルデータを辞書に格納
    data = {
        'x': [1, 0, 3, 0, 5, 0, 7, 0, 9, 0],
        'y': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        'z': [10, 8, 6, 4, 2, 0, 1, 3, 5, 7],
    }

    # 辞書からpandas DataFrameを作成
    df = pd.DataFrame(data)

    # ラインチャートのサブヘッダを表示
    st.subheader('ラインチャート')

    # pandas DataFrameを使用してラインチャートを表示
    st.line_chart(df)

if __name__ == '__main__':
    main()