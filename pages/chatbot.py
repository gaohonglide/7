import streamlit as st
import data.data as dd
import time
import datetime
# 现在有一个需求：想将数据在多个页面之间进行传递
# streamlit为多页面应用提供了一个会话session缓存器，缓存器可以存储页面变量，然后在其他页面当中获取变量进行使用
# 会话存储的变量数据只在当前浏览器中有效，如果把浏览器关闭之后重新打开，那么会话缓存的数据会自动清理
# session会话变量的基本用法
# 存储数据 st.session_state.xxx = 值
# 获取数据 res = st.session_state.xxx
# 获取缓存的用户id和用户账号
if 'user_id' not in st.session_state:
    st.session_state.user_id = 'new_user'
if 'username' not in st.session_state:
    st.session_state.username = '17335081587'

user_id = 1 # 用户id就是某一个用户的唯一标识
username = st.session_state.username
# f"字符串{变量名}"
st.title("AI智能助手 👏")
st.subheader(f"欢迎{username}使用")
st.text("这是一个AI助手，可以回答你的任何问题，请尽情使用吧！")



# 创建一个聊天输入框 接受用户输入的问题
problem = st.chat_input("请输入你的问题")
if problem:
    # 展示一个聊天信息 chat_message是一个聊天信息的展示组件，如果组件中增加信息，需要通过如下语法来完成
    with st.chat_message("user"):
        st.write(problem)
    dd.add_message(user_id,problem,role="user",message_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # AI回复一下
    with st.chat_message("assistant"):
        response = problem
        st.write(response)
    dd.add_message(user_id,response,role="assistant",message_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))










