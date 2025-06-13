# 1) 라이브러리 설치 : openai
# 2) API KEY 미지정
from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://api.upstage.ai/v1",
)

completion = client.chat.completions.create(
    # model="solar-mini", # CHANGED
    model="solar-pro2-preview",  # 7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "hello",
        }
    ],
)

print(completion.choices[0].message.content)
