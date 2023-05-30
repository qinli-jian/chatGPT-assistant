# -*- coding: utf-8 -*-

"""
-----------------------------------------------------------
Project: GPT-3.5API_test
Name: gpt_ai
Description:
Author: qinlinjian
Datetime: 2023-04-15 19:48
Product: PyCharm
-----------------------------------------------------------
"""
__author__ = "qinlinjian"
__version__ = "1.0.0"

import openai
import yaml

def chat(api_key,prompt):
    # proxies = {
    #   "http": "http://gpt.gptpoint.online:8080",
    #   "https": "http://gpt.gptpoint.online:8080",
    # }

    openai.api_key = api_key
    # openai.proxy = proxies

    # 开始调用

    # print(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    # 打印生成的文本
    print(response.choices[0].text.encode('utf-8').decode('utf-8'))
    # print(response.usage)
    return prompt+response.choices[0].text.encode('utf-8').decode('utf-8')

if __name__ == '__main__':
    api_key = ""
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)
        api_key = data["api_key"]
    # print(api_key)
    prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    while True:
        prompt = prompt+"\nHuman:"+input("Human:")
        prompt = chat(api_key,prompt)
