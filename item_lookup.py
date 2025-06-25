import streamlit as st
import pandas as pd

st.title("Tra cứu Item Value")

uploaded_file = st.file_uploader("Chọn file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Các cột hiện có:", df.columns.tolist())

    col1, col2 = st.columns(2)
    # Ô tìm kiếm Itemid
    with col1:
        item_id = st.text_input("Tìm kiếm theo Itemid")
        suggestions_id = []
        if item_id:
            # Gợi ý danh sách item id gần giống
            suggestions_id = df[df['Itemid'].astype(str).str.contains(item_id, case=False, na=False)]['Itemid'].astype(str).unique().tolist()
            if suggestions_id:
                selected_id = st.selectbox("Gợi ý Itemid:", options=[""] + suggestions_id, key="suggest_id")
                if selected_id:
                    item_id = selected_id  # Nếu chọn gợi ý, dùng giá trị này
        
    # Ô tìm kiếm Itemname
    with col2:
        item_name = st.text_input("Tìm kiếm theo Itemname")
        suggestions_name = []
        if item_name:
            # Gợi ý danh sách item name gần giống
            suggestions_name = df[df['Itemname'].astype(str).str.contains(item_name, case=False, na=False)]['Itemname'].astype(str).unique().tolist()
            if suggestions_name:
                selected_name = st.selectbox("Gợi ý Itemname:", options=[""] + suggestions_name, key="suggest_name")
                if selected_name:
                    item_name = selected_name  # Nếu chọn gợi ý, dùng giá trị này

    # Lọc dữ liệu
    filtered_df = df.copy()
    if item_id:
        filtered_df = filtered_df[filtered_df['Itemid'].astype(str).str.contains(item_id, case=False, na=False)]
    if item_name:
        filtered_df = filtered_df[filtered_df['Itemname'].astype(str).str.contains(item_name, case=False, na=False)]

    st.dataframe(filtered_df, use_container_width=True)
else:
    st.info("Hãy tải lên file Excel để tra cứu.")
