import requests
import streamlit as st
import json 


st.title("海报生成器")
# 创建一个文本输入框
form_key = st.form("my_form")
with form_key:
    input1 = st.text_input("输入您希望的背景描述")
    input2="Design Background"
    input3 = st.text_input("输入海报主标题")
    input4 ="Poster title"
    input5 = st.text_input("输入海报副标题")
    input6 ="Poster subtitle"
    user_input = st.text_input("其他：在这里输入一些海报描述文本:")
    combined_input = input2 + input1 + input4 + input3 + input6 + input5 + user_input

    apikey = st.text_input("在这里输入apikey:",type='password')
    #seeds = st.text_input("在这里输入seed:")
    style = st.radio("选择一个风格:",["GENERAL", "REALISTIC", "DESIGN"])
    ratio = st.radio("选择图片比例:",["ASPECT_10_16","ASPECT_16_9","ASPECT_1_1"])
    submitted = st.form_submit_button("提交")


if submitted:
    url = "https://api.ideogram.ai/generate"
    payload = { "image_request": {
        "model": "V_2",
        "magic_prompt_option": "AUTO",
        "prompt": combined_input,
        #"seed": seeds,
        "style_type":style,
        "aspect_ratio":ratio,
            } }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Api-Key": apikey,
    #"Api-Key": "I9KBuCdSOELKaM3S3dKDlZj2Qx1YKRFhNX72VJ4J7JQhQdk6i2xuXzap4_t7-hcLR4rczYiDRX7PVUy-GLlQXg"

        }
    response = requests.post(url, json=payload, headers=headers)
    response_json = json.loads(response.text)
    st.write(response_json)
    image_url = response_json['data'][0]['url']
    st.image(image_url, use_column_width=True)


