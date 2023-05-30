# -*- coding: utf-8 -*-

"""
-----------------------------------------------------------
Project: GPT-3.5API_test
Name: gpt_chat_api
Description:
Author: qinlinjian
Datetime: 2023-04-16 15:14
Product: PyCharm
-----------------------------------------------------------
"""
__author__ = "qinlinjian"
__version__ = "1.0.0"
import openai

proxies = {
      "http": "http://gpt.gptpoint.online:8080",
      "https": "http://gpt.gptpoint.online:8080",
    }

openai.api_key = "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"
openai.proxy = proxies
# 设置对话历史
conversation_history = [
    {"role": "system", "content": "你是一个知识问答助手，帮助用户回答各种问题，回答需要简洁地、有效地。"},
]
def chat_with_gpt_3():
    while True:
        # 调用 GPT-3 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 使用 GPT-3.5-turbo 引擎
            messages=conversation_history,
            max_tokens=2045,  # 设置最大输出长度
            n=1,
            stop=None,
            temperature=1,  # 控制输出的随机性
        )

        # 获取并打印回答
        # print(response.choices[0].message.content.encode('utf-8').decode('utf-8'))
        answer = response.choices[0].message.content.encode('utf-8').decode('utf-8')
        print("Assistant:", answer)
        # print(response.usage)
        # 如果需要，你可以将回答添加到对话历史中
        conversation_history.append({"role": "assistant", "content": answer})
        # print(conversation_history)
        user = input("user:")
        conversation_history.append({"role": "user", "content": user})

if __name__ == '__main__':
    chat_with_gpt_3()
