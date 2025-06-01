# 딕셔너리 dict() #진짜진짜 많이많이 쓴다
## 특정 key를 통해 값(value)을 찾는 것
## value에는 여러 타입이 가능하다(튜플, 셋, 리스트)
## key는 중복이 되지 않는다.

my_dict = {"me": "길동"}  # {"키":"값"}
print(my_dict)
my_dict2 = dict()
my_dict2_1 = dict([("one", "하나"), ("two", "둘")])
print(my_dict2_1)  # {'one': '하나', 'two': '둘'}
my_dict3 = {"me": [1, 2, 3], "me2": "good"}

# 데이터 추가
dict4 = dict()
dict4["max"] = [1, 2, 3, 4]  # 데이터 삽입
print(dict4)

"""
dict() 를통해 빈 딕셔너리를 만든 후

데이터 삽입을 하여 키가 4개 , 각각의 밸류에는 
다른 타입의 데이터를 넣어서 그 딕셔너리를 출력

"""
dict_a = dict()
dict_a["라면"] = ["불닭", "진라면", "틈새라면"]
dict_a["음료"] = ("포카리", "파워에이드", "토레타")
dict_a["과자"] = "빠다 코코넛", "꼬북칩", "고래밥"
dict_a["젤리"] = {"왕꿈틀이", "하리보"}
print(dict_a)

# 데이터 읽기
person = {"name": "licat", "age": 25, "height": 165.5}
print(f"이름은: {person["name"]}입니다.")
print(f"나이는: {person["age"]}입니다.")

# print(f"생년월일은:{person["good"]}") # KeyError: 'good'

# 데이터 수정
person["age"] = 30
print(person)

person = {"name": "licat", "age": 25, "height": 165.5}
person["height"] = 173.3
person["weight"] = 76.5

print(person)

# 데이터 삭제 # del 이용
del person["height"]
print(person)

person["age"] = None  # 아무것도 없다 (키를 남기고, 벨류만 삭제)

a = {"good": ["a", "b", "c"]}

a["good"].remove("c")  # 해당 value에 접근한 후, 리스트의 remove 기능 이용
print(a)  # {'good': ['a', 'b']}

b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
# {'good1': {'good2': [1, 2, 3, [1, 2, 3, 4]]}}

b["good1"]["good2"][3].append(4)
print(b)

person = {"name": "licat", "age": 25, "city": "seoul"}

# get(키,키가 없을 경우의 value)
city = person.get("city", "없는뎅")
print(city)
city2 = person.get("city2", "없는뎅")
print(city2)

person = {"name": "licat", "age": 25, "city": "seoul"}

# 키만 가져온다.
person_keys = person.keys() # 키 값들만 추출
print(person_keys)  # dict_keys(['name', 'age', 'city'])
a = list(person_keys) # 형변환
print(a)

# value만 추출
person_values = person.values() # 벨류 값들만 추출
print(person_values)
b = list(person_values)
print(b)

# 전체를 추출
person_items = person.items()
print(person_items) # dict_items([('name', 'licat'), ('age', 25), ('city', 'seoul')])
c = list(person_items) # [('name', 'licat'), ('age', 25), ('city', 'seoul')]
print(c)

# del person['age'] # 권장되지 X
a = person.pop("age") # age라는 키의 값을 a에 저장
print(a)