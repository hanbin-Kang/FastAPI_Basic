# FastAPI_Basic

Python 기반 백엔드 개발을 위한 FastAPI 학습 기록

HTTP의 기본 동작부터 시작하여 **API → JSON → FastAPI → CRUD → Database** 순서로 학습한다.

---

# 1. HTTP

## 학습 내용

* Client / Server
* HTTP
* URL
* Request / Response
* Header / Body
* HTTP Status Code
* HTTP Method

  * GET
  * POST
  * PUT
  * PATCH
  * DELETE

## 학습 자료

* 생활코딩 HTTP

## 실습

브라우저의 개발자 도구 `Network` 탭을 이용하여 실제 HTTP 통신을 확인한다.

```text
Client
   ↓
HTTP Request
   ↓
Server
   ↓
HTTP Response
   ↓
Client
```

## 학습 목표

HTTP가 무엇인지 이해하고, 클라이언트와 서버가 Request와 Response를 통해 통신하는 과정을 이해한다.

---

# 2. API

## 학습 내용

* API
* Endpoint
* Resource
* HTTP Method
* REST API
* Request
* Response
* Status Code

## 예시

```text
GET    /menus
GET    /menus/1
POST   /menus
PUT    /menus/1
DELETE /menus/1
```

API는 단순히 URL 하나를 의미하는 것이 아니라,

```text
Resource
+
Endpoint
+
HTTP Method
```

를 이용하여 서버의 기능에 접근하는 구조로 이해한다.

## 실습

API 테스트 도구를 이용하여 직접 API 요청을 보내고 Response를 확인한다.

* GET 요청
* POST 요청
* PUT / PATCH 요청
* DELETE 요청
* Status Code 확인

## 학습 목표

API의 기본 구조를 이해하고 HTTP Method에 따라 서버의 기능을 요청하는 방법을 이해한다.

---

# 3. JSON

## 학습 내용

* JSON Object
* JSON Array
* Key / Value
* 중첩 JSON
* JSON과 Python 자료구조의 관계
* API에서 JSON의 역할

## 예시

```json
{
    "name": "Americano",
    "price": 3000
}
```

여러 데이터를 표현할 수도 있다.

```json
[
    {
        "name": "Americano",
        "price": 3000
    },
    {
        "name": "Cafe Latte",
        "price": 4000
    }
]
```

## Python과 JSON

```text
Python              JSON

dict        →       Object
list        →       Array
str         →       String
int         →       Number
bool        →       Boolean
None        →       null
```

## 학습 목표

API에서 데이터를 주고받을 때 JSON이 어떤 역할을 하는지 이해한다.

---

# 4. FastAPI

## 학습 내용

* FastAPI 설치
* FastAPI 객체
* Routing
* Path Operation
* `@app.get()`
* `@app.post()`
* Path Parameter
* Query Parameter
* Request Body
* Pydantic
* Response
* Swagger UI

## 기본 구조

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}
```

## 실행

```bash
uvicorn main:app --reload
```

## API 확인

```text
/
```

Swagger UI:

```text
/docs
```

## Parameter

### Path Parameter

```text
GET /menus/1
```

```python
@app.get("/menus/{menu_id}")
def get_menu(menu_id: int):
    return {"menu_id": menu_id}
```

### Query Parameter

```text
GET /menus?name=americano
```

### Request Body

```json
{
    "name": "Americano",
    "price": 3000
}
```

Pydantic을 이용하여 요청 데이터를 정의하고 검증한다.

```python
from pydantic import BaseModel


class Menu(BaseModel):
    name: str
    price: int
```

## 학습 목표

Python 함수를 HTTP API Endpoint로 만들고, 클라이언트로부터 데이터를 받아 처리하는 FastAPI의 기본 구조를 이해한다.

---

# 5. CRUD

FastAPI를 이용하여 실제 CRUD API를 구현한다.

## CRUD

```text
Create
Read
Update
Delete
```

## API 예시

```text
GET    /todos
GET    /todos/{todo_id}
POST   /todos
PUT    /todos/{todo_id}
DELETE /todos/{todo_id}
```

## 학습 순서

```text
API 설계
   ↓
Request / Response 정의
   ↓
Endpoint 작성
   ↓
Create
   ↓
Read
   ↓
Update
   ↓
Delete
   ↓
API 테스트
```

처음에는 Database 없이 Python 자료구조를 사용하여 CRUD를 구현한다.

```python
todos = []
```

CRUD가 이해된 이후 Database를 연결한다.

## 학습 목표

FastAPI의 기본 문법을 이용하여 하나의 완성된 CRUD API를 직접 구현할 수 있도록 한다.

---

# 6. Database

FastAPI와 Database를 연결하여 실제 데이터를 저장하고 조회한다.

## 학습 내용

* ORM
* SQLAlchemy
* Model
* Session
* Database Connection
* CRUD
* FastAPI + Database
* FastAPI + Oracle

## ORM

Python 객체와 Database Table을 연결하는 개념을 이해한다.

```text
Python Object
      ↕
     ORM
      ↕
Database Table
```

## 전체 구조

```text
FastAPI
   ↓
SQLAlchemy
   ↓
Oracle
```

## 기존 Oracle Database 활용

기존에 설계한 Cafe Database를 활용한다.

```text
MENU
MEMBER
ORDERS
ORDER_DETAIL
```

## 구현 예시

```text
GET  /menus
GET  /menus/{menu_id}
POST /menus
```

이후 CRUD API와 Database를 연결하여 실제 데이터를 조회하고 추가·수정·삭제한다.

## 학습 목표

FastAPI에서 SQLAlchemy를 이용하여 Oracle Database와 연결하고 실제 데이터를 처리하는 전체 흐름을 이해한다.

---

# 학습 흐름

```text
HTTP
 ↓
API
 ↓
JSON
 ↓
FastAPI
 ↓
CRUD
 ↓
Database
```

최종적으로 다음과 같은 데이터 흐름을 이해하고 직접 구현하는 것을 목표로 한다.

```text
Client
  ↓
HTTP Request
  ↓
FastAPI
  ↓
Python Logic
  ↓
SQLAlchemy
  ↓
Oracle Database
  ↓
HTTP Response
  ↓
Client
```

---

# 학습 원칙

* 강의를 보기만 하지 않고 직접 코드를 작성한다.
* 각 개념을 배운 후 간단한 기능을 직접 구현한다.
* 모르는 개념이 나오면 필요한 범위만 추가로 학습한다.
* API를 직접 호출하여 Request와 Response를 확인한다.
* 최종적으로 FastAPI와 Database를 연결하여 직접 동작하는 API를 만든다.
