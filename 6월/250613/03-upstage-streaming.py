from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://api.upstage.ai/v1",
)

# sttream 여부에 따라, 반환겂이 다르다.
stream = client.chat.completions.create(
    model="solar-pro2-preview",  # 7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "라면 레시피를 알려줘.",
        }
    ],
    stream=True # ADDED
)


# stream=False : 통응답을 받을 때
# print(completion.choices[0].message.content)

# API 서버에서 내려준 Chunk의 개수반큼 반복된다.
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        # end 키워드 인자의 디폴트 값: 개행 ("\n")
        print(chunk.choices[0].delta.content, end="")