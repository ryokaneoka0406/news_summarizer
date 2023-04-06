import openai
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def _extract_text_from_url(url):
    """URLからテキストを抽出する関数"""
    # URLにアクセスしてHTMLを取得
    response = requests.get(url)
    response.raise_for_status()

    # HTMLをBeautifulSoupで解析し、テキストだけを抽出
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    return text

def _chat(role, prompt):
   """Chat用のヘルパー関数"""
   res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": f"You are {role}"},
        {"role": "user", "content": prompt},
        ]
        )
   return res

def _prompt(url):
   """要約を行うためのプロンプトを作成する関数"""
   prompt_1h = """
   指示：
   次の文章をわかりやすい日本語の箇条書き10個程度で要約してください。

   文章：
   """
   res = _extract_text_from_url(url)

   prompt_2h = """
   要約結果：
   """
   return prompt_1h + res + prompt_2h

def summarize(url):
   """要約を行う関数"""
   prompt = _prompt(url)
   res = _chat("a powerful summary machine", prompt)
   return res

url = input("URLを入力してください：")
print(summarize(url)['choices'][0]['message']['content'])