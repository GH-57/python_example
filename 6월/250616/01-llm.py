
# .env 파일을 일겅서, 환경변수로서 로딩
# - python-dotenv
# - django-environ

from environ import Env
from pathlib import Path

# __file__: 현재 소스파일의 경로
# cf. -> __name__: 현재 소스파일의 모듈명


BASE_DIR = Path(__file__).parent
ENV_PATH = BASE_DIR / ".env"

env = Env()
# 디폴트로 같은 이름의 환경변수가 있다면, 무시합니다
# 덮어쓰려면 overwrite=True 인자룰 지정한다
env.read_env(ENV_PATH, overwrite=True)

import os
print(os.environ["HELLO"])
