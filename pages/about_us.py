import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from Modules import VisualHandler

# Cấu hình trang
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
VisualHandler.initial()

# Hàm hiển thị thông tin về CALM
def display_about_info():
    st.title("About CALM")
    # Câu chuyện về CALM
    with st.expander("Câu chuyện về CALM", expanded=False):
        st.write("""
            Bạn có bao giờ đứng trước gian bếp với hàng tá nguyên liệu mà không biết làm món gì? 
            Chào mừng đến với CALM, nơi bạn có thể tìm thấy vô số công thức nấu ăn đa dạng. 
            Mỗi công thức đều được trình bày chi tiết, kèm theo hình ảnh minh họa và mẹo nhỏ giúp bạn dễ dàng thực hiện dù là lần đầu vào bếp. 
            Đặc biệt, với giao diện thân thiện và các công cụ tìm kiếm tiện lợi, bạn có thể chọn món theo nguyên liệu và tình trạng sức khỏe. 
            Hãy để mỗi bữa ăn trở thành một trải nghiệm thư giãn và khám phá từng món ăn mỗi ngày cùng chúng tôi!
        """)

    # Slogan
    with st.expander("Slogan |n_n|", expanded=False):
        st.subheader('"Health - Nutrition - Happiness"')
        st.write("""
            Sứ mệnh của CALM là truyền cảm hứng để mọi người trải nghiệm bữa ăn lành mạnh, đầy đủ dinh dưỡng và tràn ngập niềm vui. 
            Chúng tôi luôn hướng đến các công thức chế biến theo cách tối ưu nhất để giữ trọn giá trị dinh dưỡng. 
            Mỗi món đều cung cấp đủ dưỡng chất cần thiết, đảm bảo sự cân bằng giữa hương vị và sức khỏe. 
            Không chỉ là những món ăn, chúng tôi mong muốn bạn sẽ tìm thấy niềm vui, sự thư giãn và cảm giác hạnh phúc khi tự tay chế biến 
            và thưởng thức những bữa ăn bổ dưỡng bên gia đình.
        """)

    # Dịch vụ của chúng tôi
    with st.expander("Dịch vụ của chúng tôi", expanded=False):
        offers = {
            "Hướng dẫn nấu ăn theo nguyên liệu sẵn có": """
                CALM giúp bạn dễ dàng tìm được ý tưởng món ăn từ những nguyên liệu có sẵn trong bếp. 
                Với tính năng này, bạn chỉ cần nhập các nguyên liệu hiện có, hệ thống sẽ đưa ra các gợi ý món ăn đa dạng và phân loại theo độ khó, 
                từ những món ăn đơn giản cho ngày bận rộn đến các công thức sáng tạo. Ngoài ra, mỗi món ăn còn được gợi ý dựa trên mức độ phù hợp 
                với tình trạng sức khỏe của bạn, giúp bạn dễ dàng lựa chọn công thức lý tưởng cho mọi bữa ăn.
            """,
            "Xây dựng thực đơn cá nhân hóa": """
                CALM còn hỗ trợ bạn xây dựng thực đơn cá nhân hóa một cách khoa học và hiệu quả dựa trên chỉ số BMI, ngân sách và mục tiêu dinh dưỡng của riêng mình. 
                CALM mang đến giải pháp tối ưu giúp bạn tiết kiệm thời gian, tối đa hóa dinh dưỡng và duy trì lối sống lành mạnh 
                với thực đơn được cá nhân hóa trong từng món ăn.
            """
        }

        for offer, descript in offers.items():
            st.subheader(offer)
            st.write(descript)
           
            st.markdown("""
                <style>
                    .stButton > button {
                        width: 300px;  /* Điều chỉnh chiều rộng */
                        height: 35px;  /* Điều chỉnh chiều cao */
                        font-size: 14px;  /* Kích thước chữ */
                        border-radius: 5px;  /* Làm bo góc */
                        padding: 5px;  /* Padding để chữ không bị sát viền */
                    }
                </style>
            """, unsafe_allow_html=True)

            if offer == "Hướng dẫn nấu ăn theo nguyên liệu sẵn có":
                # Sử dụng switch_page để điều hướng đến Recipe khi nhấn nút
                if st.button('Xem chi tiết về công thức nấu ăn'):
                    switch_page('Recipe')
            else:
                # Sử dụng switch_page để điều hướng đến Make Menu khi nhấn nút
                if st.button('Xem chi tiết về xây dựng thực đơn'):
                    switch_page('Make Menu')

    # Let’s start with CALM
    with st.expander("Let’s start with CALM", expanded=False):
        st.write("""
            CALM mong muốn là người bạn đồng hành đáng tin cậy trên hành trình ẩm thực của bạn. 
            Bất kể bạn đang tìm kiếm một bữa ăn nhanh cho gia đình, hay một thực đơn cân bằng dinh dưỡng, 
            CALM luôn ở đây để hỗ trợ. Hãy cùng chúng tôi bắt đầu hành trình ẩm thực ngay hôm nay và 
            biến mỗi bữa ăn thành một trải nghiệm đáng nhớ!
        """)

# Hiển thị thông tin về CALM
display_about_info()