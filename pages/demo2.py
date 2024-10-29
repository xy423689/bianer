'''
大模型对象
提示词对象
链chain:将大模型对象和提示词联系起来
'''
#制作聊天界面
import streamlit as st
from langchain_openai import ChatOpenAI
#引用提示词对象
from langchain.prompts import PromptTemplate
#链对象
from langchain.chains import LLMChain
#解决重新加载的问题  重新加载的时候保证聊天记录不会清空
#构建大模型 智谱
model=ChatOpenAI(
    temperature=0.8,#创新性
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="e210867e75503a51d642ec7f809cab2f.pNhLRYP2pdFLfjuJ",

)
#提示词对象
prompt=PromptTemplate.from_template("你的名字是小李，你现在是一个好脾气，情商高，三观正的男朋友{input}")
#关联
chain=LLMChain(
    llm=model,
    prompt=prompt,
)
st.title("小辫儿~")
#构建缓存保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])

#创建聊天输入框
problem =st.chat_input("小辫儿在等待")
#确定问题被输入
if problem:
#输入问题 、调用大模型回答问题 、将大模型回答的问题输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})
    result=chain.invoke({"input":problem})
    with st.chat_message("assistant"):
         st.write(result["text"])
    st.session_state.cache.append({"role": "assistant", "content": result['text']})