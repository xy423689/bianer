#制作聊天界面
import streamlit as st
from langchain_openai import ChatOpenAI
#构建大模型 智谱
model=ChatOpenAI(
    temperature=0.8,#创新性
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="e210867e75503a51d642ec7f809cab2f.pNhLRYP2pdFLfjuJ",#
)
st.title("Hi~~~")
#创建聊天输入框
problem =st.chat_input("请输入你的问题")
#确定问题被输入
if problem:
#输入问题 、调用大模型回答问题 、将大模型回答的问题输出
    with st.chat_message("user"):
        st.write(problem)
    result=model.invoke(problem)
    with st.chat_message("assistant"):
        st.write(result.content)