import streamlit as st

st.title("模型")
col1, col2 = st.columns(2)
with col1:
    st.image('https://ts1.cn.mm.bing.net/th/id/R-C.9881613a29f26488b40938427aa585e4?rik=fim4XvDejjHE%2fQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20220516ac%2f797%2fw2048h1149%2f20220516%2fb0aa-5aca29fe2dfa69c385118bbc74d039de.jpg&ehk=tzq%2bJP6uMipI0aIHY3bMSVO7lS7ZQM6TKMlwZ5CFP4s%3d&risl=&pid=ImgRaw&r=0',use_column_width=True)
    flag=st.button("大智慧",use_container_width=True)
    if flag:
        st.switch_page("pages/demo3.py")
with col2:
    st.image('https://ts1.cn.mm.bing.net/th/id/R-C.9881613a29f26488b40938427aa585e4?rik=fim4XvDejjHE%2fQ&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20220516ac%2f797%2fw2048h1149%2f20220516%2fb0aa-5aca29fe2dfa69c385118bbc74d039de.jpg&ehk=tzq%2bJP6uMipI0aIHY3bMSVO7lS7ZQM6TKMlwZ5CFP4s%3d&risl=&pid=ImgRaw&r=0',use_column_width=True)
    flag1=st.button("大智慧儿",use_container_width=True)
    if flag1:
        st.switch_page("pages/textToimage.py")

# c1,c2,c3,c4 ,c5= st.columns(5)
# with c1:
#     flag=st.button("青铜")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1=st.button("钻石")
#     if flag1:
#         st.switch_page("pages/demo1.py")
#
# with c3:
#     flag2=st.button("星耀")
#     if flag2:
#         st.switch_page("pages/demo2.py")
#
# with c4:
#     flag3=st.button("王者")
#     if flag3:
#         st.switch_page("pages/demo3.py")
# with c5:
#     flag3=st.button("文生图")
#     if flag3:
#         st.switch_page("pages/textToimage.py")
