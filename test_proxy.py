# -*- coding: utf-8 -*-

"""
-----------------------------------------------------------
Project: GPT-3.5API_test
Name: test_proxy
Description:
Author: qinlinjian
Datetime: 2023-04-15 19:58
Product: PyCharm
-----------------------------------------------------------
"""
__author__ = "qinlinjian"
__version__ = "1.0.0"
import requests

proxies = {
  "http": "http://52.43.164.8:8080",
  "https": "http://52.43.164.8:8080",
}

api_key = "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"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "介绍一下你，你是哪个版本？"}],
}

response = requests.post("https://api.openai.com/v1/chat/completions",
                         json=data,
                         headers=headers,
                         proxies=proxies)

print(response.json())
print(response.json()['choices'][0]['message']['content'])

