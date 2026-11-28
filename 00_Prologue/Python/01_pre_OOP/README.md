# OOP 들어가기 전에 개념 정리

[함수]

[파이썬 메모리 구조]

## 예외 처리 (Exception Handling)

## 1. 오류(Error)의 종류

프로그램에서 발생하는 오류는 크게 두 가지로 구분할 수 있다.

### (1) Syntax Error [구문 오류]

- 프로그램의 문법이 잘못되어 발생하는 오류
- 프로그램 실행 전에 파이썬이 코드를 해석하는 과정에서 발생
- 오류가 있으면 프로그램이 정상적으로 실행되지 않음

```python
if True
    print("Hello")
```

콜론(`:`)이 누락되어 SyntaxError 발생

### (2) Runtime Error [실행 시간 오류 / Exception]

- 프로그램 실행 중에 발생하는 오류
- 오류가 발생하기 전까지의 코드는 실행됨
- 예외 처리를 통해 프로그램이 비정상적으로 종료되는 것을 방지할 수 있음

```python
num = 10
result = num / 0  # ZeroDivisionError
print(result)
```

0으로 나누는 순간 예외 발생

---

## 2. 예외 처리 방법

### (1) if - elif - else

조건문을 사용하여 예외가 발생할 수 있는 상황을 미리 검사하는 방법

```python
num = int(input("숫자 입력> "))

if num == 0:
    print("0은 사용할 수 없습니다.")
else:
    print(10 / num)
```

- 예측 가능한 조건을 직접 검사할 때 사용
- 예외의 종류가 많거나 예상하지 못한 오류까지 처리하기에는 한계가 있음

### (2) try - except

예외가 발생할 가능성이 있는 코드를 `try`에 작성하고, 예외가 발생하면 `except`에서 처리하는 방법

```python
try:
    num = int(input("숫자 입력> "))
    print(10 / num)

except ValueError:
    print("숫자를 입력해주세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
```

- `try` : 예외가 발생할 가능성이 있는 코드
- `except` : 특정 예외가 발생했을 때 실행할 코드
- 여러 개의 `except`를 사용하여 예외 종류별로 구분 가능
- 예외가 발생하면 해당 `try` 블록의 나머지 코드는 실행하지 않고 예외 처리로 이동

### (3) else

`try` 블록에서 예외가 발생하지 않았을 때 실행하는 구문

```python
try:
    num = int(input("숫자 입력> "))
    result = 10 / num

except ValueError:
    print("숫자를 입력해주세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

else:
    print(f"결과: {result}")
    print("계산 성공!")
```

- 예외가 발생하지 않았을 때만 실행
- `except`와 달리 정상적으로 실행되었을 때 수행할 코드를 작성

### (4) finally

예외 발생 여부와 관계없이 무조건 실행되는 구문

```python
try:
    num = int(input("숫자 입력> "))
    print(10 / num)

except ValueError:
    print("숫자를 입력해주세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

else:
    print("계산 성공!")

finally:
    print("프로그램 종료")
```

- 예외 발생 여부와 관계없이 실행
- 파일 닫기, 자원 정리 등 마무리 작업에 사용

### try-except-else-finally 구조

```python
try:
    # 예외가 발생할 가능성이 있는 코드

except 예외객체:
    # 예외가 발생했을 때 실행

else:
    # 예외가 발생하지 않았을 때 실행

finally:
    # 예외 발생 여부와 관계없이 실행
```

---

## 3. 예외 객체 (Exception Object)

예외가 발생했을 때 예외와 관련된 정보를 담고 있는 객체

### 주요 예외 객체

| 예외 객체 | 발생 원인 |
|---|---|
| NameError | 정의되지 않은 변수나 이름을 사용했을 때 |
| ValueError | 자료형은 맞지만 적절하지 않은 값을 사용했을 때 |
| TypeError | 연산이나 함수에 잘못된 자료형을 사용했을 때 |
| IndexError | 리스트 등에 존재하지 않는 인덱스에 접근했을 때 |
| ZeroDivisionError | 숫자를 0으로 나누려고 할 때 |
| FileNotFoundError | 존재하지 않는 파일을 열려고 할 때 |
| Exception | 일반적인 예외들의 부모 클래스 |

### 예외 객체의 상속 관계

- `Exception`은 대부분의 일반적인 실행 시간 예외 클래스의 부모 클래스
- 따라서 구체적인 예외를 먼저 작성하고 `Exception`을 마지막에 작성해야 함

```python
try:
    num = int("hello")

except ValueError:
    print("값 오류")

except Exception:
    print("기타 예외")
```

주의: `Exception`보다 상위에는 `BaseException`이 존재하며, 모든 예외를 무조건 `Exception`이 잡는 것은 아님.

### 예외 객체의 정보 확인

`as`를 사용하면 발생한 예외 객체를 변수에 저장할 수 있음.

```python
try:
    num = int("hello")

except ValueError as e:
    print(e)
```

- `e` : 발생한 예외 객체
- `print(e)` : 예외와 관련된 메시지 출력

---

## 4. 예외를 강제로 발생시키기 (raise)

`raise`를 사용하면 개발자가 직접 예외를 발생시킬 수 있음.

### 기본 문법

```python
raise 예외객체()
```

### 사용 예시

```python
score = 150

if score < 0 or score > 100:
    raise ValueError("점수는 0~100 사이여야 합니다.")
```

실행 결과

```text
ValueError: 점수는 0~100 사이여야 합니다.
```

### 사용 목적

- 잘못된 입력이나 조건을 개발자가 직접 검사하고 예외 발생
- 프로그램에서 허용하지 않는 상황을 명확하게 알림
- 예외를 호출한 곳으로 전달하여 처리하도록 할 수 있음

### pass와 raise의 차이

| 구문 | 역할 |
|---|---|
| pass | 아무 작업도 하지 않고 넘어감 |
| raise | 예외를 직접 발생시킴 |

`pass`는 예외를 발생시키거나 전달하지 않음. 단순히 실행할 코드가 없을 때 사용하는 구문임.

---

## 5. 핵심 정리

| 구문 | 핵심 역할 |
|---|---|
| try | 예외가 발생할 가능성이 있는 코드 실행 |
| except | 예외 발생 시 처리 |
| else | 예외가 발생하지 않았을 때 실행 |
| finally | 예외 발생 여부와 관계없이 실행 |
| raise | 예외를 직접 발생시킴 |
| as | 예외 객체를 변수에 저장 |

**기억할 점**
1. 예외는 프로그램 실행 중 발생하는 오류를 의미한다.
2. `try-except`는 예외 종류에 따라 대응할 수 있도록 해준다.
3. 구체적인 예외를 먼저 작성하고 `Exception`은 마지막에 작성한다.
4. `else`는 예외가 없을 때, `finally`는 예외 발생 여부와 관계없이 실행된다.
5. `raise`는 개발자가 직접 예외를 발생시킬 때 사용한다.