import streamlit as st
from zhipuai import ZhipuAI

model = ZhipuAI(api_key="e210867e75503a51d642ec7f809cab2f.pNhLRYP2pdFLfjuJ")
st.title('请胡思乱想，剩下的交给我')

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role'] == "user":
            with st.chat_message(message['role']):
                st.write(message["content"])

desc = st.chat_input("请输入内容")
if desc:
    with st.chat_message("user"):
        st.write(desc)
    response = model.images.generations(
        model="cogview-3-plus",  # 填写需要调用的模型编码
        prompt=desc,
    )
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=300)
    st.session_state.cache.append({"role": "assistant", "content": desc})