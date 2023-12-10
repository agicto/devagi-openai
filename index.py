import os
import openai

# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# print(find_dotenv())
# 配置 OpenAI 服务
# openai.api_key = os.getenv("OPENAI_API_KEY")  # 设置 OpenAI 的 key
# openai.api_base = os.getenv("OPENAI_BASE_URL")  # 指定代理地址

import openai

response =openai.ChatCompletion.create(
  model="gpt-4",
  # model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "你是一个精通Python语言的编程专家。"},
        {"role": "user", "content": "Python有什么特点?"}
    ],
  temperature=0
)

print(response)
# print(response['choices'][0]['message']['content'])







