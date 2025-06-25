import streamlit as st
import pandas as pd

st.title("Tra cứu Item Value")

# 1. Upload file Excel
uploaded_file = st.file_uploader("Chọn file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    # Đọc dữ liệu từ Excel
    df = pd.read_excel(uploaded_file)
    
    # 2. Filter/Search theo Item ID hoặc Item Name
    col1, col2 = st.columns(2)
    with col1:
        item_id = st.text_input("Tìm kiếm theo Item ID")
    with col2:
        item_name = st.text_input("Tìm kiếm theo Item Name")
    
    # Lọc dữ liệu
    filtered_df = df.copy()
    if item_id:
        filtered_df = filtered_df[filtered_df['item id'].astype(str).str.contains(item_id, case=False, na=False)]
    if item_name:
        filtered_df = filtered_df[filtered_df['item name'].astype(str).str.contains(item_name, case=False, na=False)]
    
    # 3. Hiển thị dữ liệu
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.info("Hãy tải lên file Excel để tra cứu.")

