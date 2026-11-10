# WEB1 - HTML

생활코딩 WEB1 강의를 통해 HTML의 기본 구조와 주요 태그, 속성, 부모-자식 관계를 학습한다.

---

## 1. HTML 파일

HTML 파일의 확장자는 `.html`을 사용한다.

```text
index.html
```

Mac에서는 `cmd + o`를 사용하여 HTML 파일을 브라우저에서 열 수 있다.

---

## 2. TAG

HTML은 **TAG(태그)**를 사용하여 웹페이지의 구조와 내용을 표현한다.

```html
<strong>내용</strong>
```

일반적인 태그는 여는 태그와 닫는 태그로 구성된다.

```html
<태그>내용</태그>
```

### `<strong>`

텍스트를 굵게 표시한다.

```html
<strong>중요한 내용</strong>
```

### `<u>`

텍스트에 밑줄을 표시한다.

```html
<u>밑줄이 있는 내용</u>
```

### `<h1> ~ <h6>`

웹페이지의 제목을 나타낸다.

`h1`이 가장 중요한 최상위 제목이며 숫자가 커질수록 하위 제목이 된다.

```html
<h1>HTML</h1>
<h2>HTML이란?</h2>
<h3>HTML의 특징</h3>
```

### `<br>`

줄바꿈을 한다.

내용을 감싸는 태그가 아니기 때문에 닫는 태그가 필요하지 않다.

```html
첫 번째 줄<br>
두 번째 줄
```

### `<p>`

문단을 구분한다.

```html
<p>첫 번째 문단입니다.</p>
<p>두 번째 문단입니다.</p>
```

`<br>`과 달리 문단이라는 의미를 HTML에 명확하게 전달할 수 있다.

문단 사이의 간격을 조절하려면 CSS를 사용할 수 있다.

```html
<p style="margin-top:40px;">
    문단 내용
</p>
```

### `<img>`

웹페이지에 이미지를 삽입한다.

```html
<img src="coding.jpg">
```

이미지의 크기도 속성을 사용하여 지정할 수 있다.

```html
<img src="coding.jpg" width="80%">
```

---

## 3. 목록

### `<li>`

List Item의 약자로 목록의 각 항목을 나타낸다.

```html
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
```

`<li>`는 일반적으로 `<ul>` 또는 `<ol>`과 함께 사용한다.

### `<ul>`

Unordered List의 약자로 **순서가 없는 목록**을 만든다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

결과:

```text
• HTML
• CSS
• JavaScript
```

### `<ol>`

Ordered List의 약자로 **순서가 있는 목록**을 만든다.

번호가 자동으로 표시되기 때문에 번호를 직접 작성할 필요가 없다.

```html
<ol>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

결과:

```text
1. HTML
2. CSS
3. JavaScript
```

---

## 4. 부모와 자식 관계

HTML 태그는 서로 **부모-자식 관계**를 가질 수 있다.

특히 `<ul>`, `<ol>`과 `<li>`가 대표적인 예이다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

구조를 보면 다음과 같다.

```text
<ul>       ← 부모
 ├─ <li>   ← 자식
 ├─ <li>   ← 자식
 └─ <li>   ← 자식
```

즉, `<ul>` 안에 `<li>`가 포함되는 구조이다.

```text
ul
└── li
```

또는

```text
ol
└── li
```

형태로 사용한다.

---

## 5. HTML 문서의 기본 구조

HTML 문서는 기본적으로 다음과 같은 구조를 가진다.

```html
<html>
    <head>
    </head>

    <body>
    </body>
</html>
```

구조를 보면 다음과 같다.

```text
<html>
 ├── <head>  → 문서의 정보와 설정
 └── <body>  → 실제 웹페이지에 표시되는 내용
```

---

## 6. `<head>`

웹페이지에 직접 표시되는 내용보다는 **문서의 정보와 설정**을 작성하는 영역이다.

```html
<head>
    ...
</head>
```

### `<title>`

브라우저의 탭에 표시되는 웹페이지의 제목을 설정한다.

```html
<title>WEB1 - HTML</title>
```

### `<meta>`

HTML 문서에 대한 메타데이터를 설정한다.

문자 인코딩을 지정할 때 사용할 수 있다.

```html
<meta charset="utf-8">
```

---

## 7. `<body>`

실제 웹페이지에 표시되는 내용을 작성하는 영역이다.

```html
<body>
    <h1>HTML</h1>
    <p>HTML을 공부하고 있습니다.</p>
</body>
```

---

## 8. 링크

웹페이지에서 다른 페이지로 이동할 수 있도록 링크를 만들 수 있다.

### `<a>`

`a`는 Anchor의 약자로 **링크를 만드는 태그**이다.

```html
<a href="https://www.google.com">Google</a>
```

`<a>`를 다른 페이지로 이동하는 **길(way)**이라고 생각하면 이해하기 쉽다.

```text
<a>
 ↓
링크 생성
 ↓
href
 ↓
이동할 주소 지정
```

---

## 9. `<a>`의 주요 속성

### `href`

링크가 이동할 주소를 지정한다.

```html
<a href="https://www.google.com">
    Google
</a>
```

### `target`

링크를 여는 방법을 지정한다.

`_blank`를 사용하면 새 탭에서 열린다.

```html
<a href="https://www.google.com" target="_blank">
    Google
</a>
```

### `title`

링크에 마우스를 올렸을 때 설명을 표시한다.

```html
<a href="https://www.google.com"
   title="Google로 이동">
    Google
</a>
```

---

## 10. 속성(Attribute)

태그만으로는 표현하기 부족한 추가 정보를 **속성(Attribute)**으로 지정할 수 있다.

기본 형태:

```html
<태그 속성="값">내용</태그>
```

예를 들어 `<img>` 태그에 이미지의 위치와 크기를 지정할 수 있다.

```html
<img src="coding.jpg" width="80%">
```

각각의 의미는 다음과 같다.

```text
<img>              → 태그
src="coding.jpg"   → 이미지의 위치
width="80%"        → 이미지의 너비
```

즉, **속성은 태그에 추가적인 정보를 제공한다.**

---

## 11. 전체 HTML 구조 예시

지금까지 배운 내용을 하나의 HTML 문서로 작성하면 다음과 같다.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>WEB1 - HTML</title>
        <meta charset="utf-8">
    </head>

    <body>
        <h1>HTML</h1>

        <p>
            <strong>HTML</strong>은
            <u>웹페이지</u>를 만드는 언어이다.
        </p>

        <h2>목차</h2>

        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>

        <p>
            <a href="https://www.google.com"
               target="_blank"
               title="Google로 이동">
                Google
            </a>
        </p>

        <img src="coding.jpg" width="80%">
    </body>
</html>
```

---

## 12. 핵심 정리

| 태그 / 속성 | 역할 |
|---|---|
| `<strong>` | 굵게 표시 |
| `<u>` | 밑줄 표시 |
| `<h1> ~ <h6>` | 제목 |
| `<br>` | 줄바꿈 |
| `<p>` | 문단 |
| `<img>` | 이미지 삽입 |
| `<li>` | 목록의 항목 |
| `<ul>` | 순서 없는 목록 |
| `<ol>` | 순서 있는 목록 |
| `<html>` | HTML 문서 전체 |
| `<head>` | 문서 정보 및 설정 |
| `<body>` | 실제 웹페이지 내용 |
| `<title>` | 브라우저 탭 제목 |
| `<meta>` | 문서의 메타데이터 |
| `<a>` | 링크 |
| `href` | 링크 주소 |
| `target` | 링크를 여는 방법 |
| `title` | 마우스를 올렸을 때 표시할 설명 |
| `src` | 이미지 등의 리소스 위치 |
| `width` | 이미지 너비 |

---

## 13. 핵심 개념

### 태그

HTML의 구조와 내용을 표현한다.

```html
<h1>제목</h1>
<p>문단</p>
```

### 속성

태그에 추가적인 정보를 제공한다.

```html
<img src="coding.jpg" width="80%">
```

### 부모와 자식

태그가 다른 태그를 포함할 수 있다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

```text
ul
├── li
└── li
```

### 링크

`<a>` 태그와 `href` 속성을 사용하여 다른 페이지로 이동할 수 있다.

```html
<a href="https://www.google.com">
    Google
</a>
```