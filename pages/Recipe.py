#PART 1
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
import pandas as pd
from Modules import VisualHandler

st.set_page_config(
    page_title="Recipe",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="collapsed",
)
VisualHandler.initial()



#############################################################################################################

with open("ingredients.json", "r", encoding="utf-8") as file:
    ingredients_data = json.load(file)
medical_conditions = ["Tiểu đường", "Huyết áp cao", "Dạ dày", "Gout"]
st.markdown("""
    <style>
    .ingredient-box {
        display: inline-block;
        background-color: #ffffff; /* White background */
        color: #333;
        border: 2px solid #dcdcdc; /* Light gray border */
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
        text-align: center;
        font-weight: bold;
        width: 100%;
        font-size: 18px;
    }
    .ingredient-box input[type="checkbox"] {
        accent-color: #4CAF50; /* Checkbox color */
        transform: scale(1.2); /* Make the checkbox slightly larger */
    }
    </style>
""", unsafe_allow_html=True)

selected_ingredients = []
selected_conditions = []
st.title("Gợi ý món ăn")
display = False

df = pd.read_csv("foods.csv")

def similarity(list1, list2):
    set1 = set(list1.split(","))
    set2 = set(list2)
    return len(set1.intersection(set2))

def link_create(ten_mon):
    row = df.loc[df['Tên món'] == ten_mon]
    return row['Công thức'].values[0]

with st.sidebar:
    st.title("Chọn nguyên liệu")
    for category, items in ingredients_data.items():
        st.markdown(f"**{category}**")
        ingredient_columns = st.columns(3)
        for i, ingredient in enumerate(items):
            with ingredient_columns[i % 3]:
                if st.checkbox(ingredient, key=f"{category}_{ingredient}"):
                    selected_ingredients.append(ingredient)

    st.title("Bệnh lý")
    condition_columns = st.columns(2)
    for i, condition in enumerate(medical_conditions):
        with condition_columns[i % 2]:
            if st.checkbox(condition, key=f"condition_{condition}"):
                selected_conditions.append(condition)

    button_column = st.columns([2, 1])  
    with button_column[1]: 
        if st.button("Xác nhận", key="confirm_button"):
            display = True
#############################################################################################################
import streamlit as st
from fuzzywuzzy import process
import pandas as pd

# Thanh tìm kiếm món ăn
st.title("Tìm kiếm món ăn")
search_query = st.text_input("Nhập tên món ăn:", "")  # Chỉ tạo một thanh tìm kiếm

if search_query:
    # Tìm món ăn dựa trên độ tương đồng cao nhất
    suggestions = process.extract(search_query, df["Tên món"], limit = 20) 

    if suggestions:
        st.markdown("### Kết quả tìm kiếm:")
        selected_recipe = st.selectbox(
            "Chọn một món ăn từ gợi ý:",
            options=[suggestion[0] for suggestion in suggestions],  # Chỉ lấy tên món ăn
            key="unique_selectbox"  # Đảm bảo không tạo thêm selectbox trùng lặp
        )

        # Hiển thị thông tin món ăn nếu người dùng chọn món
    if selected_recipe:
        selected_row = df[df["Tên món"] == selected_recipe].iloc[0]
        
        # Thay thế phần st.markdown ban đầu bằng phần HTML có style
        st.markdown(
            f"""
            <div style="background-color:#e8ea8c; padding: 20px; border-radius: 10px; 
                        border: 2px solid #e8ea8c;">
                <h3 style="color:black;">{selected_row['Tên món']}</h3>
                <p style="color:black;"><strong>Nguyên liệu chính:</strong> {selected_row['Nguyên liệu']}</p>
                <p style="color:black;"><strong>Thời gian nấu:</strong> {selected_row['Time']}</p>
                <p style="color:black;"><strong>Calo:</strong> {selected_row['Calo ']} kcal</p>
                <a href="{selected_row['Công thức']}" target="_blank">
                    <button style="padding: 8px 12px; color: white; background-color: #4CAF50; 
                                border: none; border-radius: 5px; cursor: pointer;">
                        Xem công thức
                    </button>
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.info("Không tìm thấy món ăn phù hợp với từ khóa của bạn.")


#############################################################################################################

default_dishes = ['Tôm chiên xù','Canh rau dền nấu mọc tôm',"Su su xào thịt bò","Bò Xào Nấm Kim Châm",
                'Trứng chiên thịt nấm hương','Canh gà nấu cá nấm','Vịt om sấu','Tôm hấp bia',
                'Thịt lợn kho trứng cút','Canh rau cần','Mực nhồi thịt sốt dầu hào','Ức gà cuộn nấm kim châm']
df_filtered = df_filtered = df[df['Tên món'].isin(default_dishes)]

if not display:# and not search_input:
    st.title("BEST SELLERS!!!")
    cols = st.columns(3)
    for index, row in df_filtered.reset_index(drop=True).iterrows():
        col = cols[index % 3]
        with col:
            with st.container():
                st.markdown(
                f"""
                <div style="background-color:#e8ea8c; padding: 20px; border-radius: 10px; 
                            border: 2px solid #e8ea8c;">
                    <h3 style="color:black;">{row[0]}</h3>
                    <p style="color:black;"><strong>Nguyên liệu chính:</strong> {row[1]}</p>
                    <p style="color:black;"><strong>Thời gian:</strong> {row[7]}</p>
                    <p style="color:black;"><strong>Calo:</strong> {row[8]} kcal</p>
                    <a href="{link_create(row[0])}" target="_blank">
                        <button style="padding: 8px 12px; color: white; background-color: #4CAF50; 
                                    border: none; border-radius: 5px; cursor: pointer;">
                            Xem công thức
                        </button>
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)

elif display:
    if selected_conditions:
        conditions = [~(df[col] == 1) for col in selected_conditions]
        df_loc = df[pd.concat(conditions, axis=1).all(axis=1)]
    else:
        df_loc = df.copy()
    if not selected_ingredients:
        st.warning("Vui lòng chọn nguyên liệu mà bạn có.")
    else:
        df["similarity"] = df["Nguyên liệu"].apply(lambda x: similarity(x, selected_ingredients))
        df_filtered = df[df["similarity"] > 0]
            
        if df_filtered.empty:
            st.info("CALM KITCHEN hiện tại chưa có món ăn phù hợp cho nguyên liệu của bạn.")
        else:
            df_filtered = df_filtered.sort_values("similarity", ascending=False)

        cols = st.columns(3)
        for index, row in df_filtered.reset_index(drop=True).iterrows():
            col = cols[index % 3]
            with col:
                with st.container():
                    st.markdown(
                    f"""
                        <div style="background-color:#e8ea8c; padding: 20px; border-radius: 10px; 
                                    border: 2px solid #e8ea8c;">
                            <h3 style="color:black;">{row[0]}</h3>
                            <p style="color:black;"><strong>Nguyên liệu chính:</strong> {row[1]}</p>
                            <p style="color:black;"><strong>Thời gian:</strong> {row[7]}</p>
                            <p style="color:black;"><strong>Calo:</strong> {row[8]} kcal</p>
                            <a href="{link_create(row[0])}" target="_blank">
                                <button style="padding: 8px 12px; color: white; background-color: #4CAF50; 
                                            border: none; border-radius: 5px; cursor: pointer;">
                                    Xem công thức
                                </button>
                            </a>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                st.markdown("<br>", unsafe_allow_html=True)