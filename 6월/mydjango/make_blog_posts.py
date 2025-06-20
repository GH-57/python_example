# 이 파일은 장고 프로젝트 외적인 파일입니다.
# 장고 밖에서 장고의 리소스를 활용해보고
# LLM을 통해서 블로그 포스팅을 생성해보겠습니다.

# 모든 장고를 활용하려는 파이썬 코드는 무조건 DJANGO_SETTINGS_MODULE 환경변수 지정이 필요하다
# 현재의 파이썬 코드를 통해 사용할 settings의 경로를 알려줘야만 한다.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

# 이제 장고 리소스를 활용할 준비가 되었다

from pyhub.llm import OpenAILLM, UpstageLLM
from django.conf import settings
from pydantic import BaseModel

class BlogPost(BaseModel):
    title: str
    content: str

llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    model="gpt-4o-mini", # dall-e-3 이미지 생성 ai
    system_prompt="""너는 여행 블로거야. 쥬어가 제시하는 내용에 맞춰, 블로그의 제모과 내용을 작성해줘""",
)
reply = llm.ask("대전 성심당 튀김소보로")

title = reply.text.splitlines()[0]
content = "\n".join(reply.text.splitlines()[1:])

print("# title :", title)
print("----")
print(content)

# Post 임포트 하시고 나서
# Post.objects.create(title=title, content=content)  
# - 수행하시면, 데이터베이스에 저장이 됩니다.
# print(reply.text) # st 타입: 제목과 내용이 붙어 나온다

# from blog.models import Post
# qs = Post.objects.all()
# print("posts :", qs)