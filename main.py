import streamlit as st
import numpy as np
import pandas as pd

def main():
    data = {
        'x': [1, 0, 3, 0, 5, 0, 7, 0, 9, 0],
        'y': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        'z': [10, 8, 6, 4, 2, 0, 1, 3, 5, 7],
    }
    df = pd.DataFrame(data)
    st.subheader('Line Chart')
    st.line_chart(df)

if __name__ == '__main__':
    main()