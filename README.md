# Alfred 5 Workflow - Custom Web search
- Whale 브라우저를 통한 현재 탭에서 빠른 검색, Whale 브라우저를 통한 새로운 윈도우에서 빠른 검색
- Chrome 브라우저를 통한 현재 탭에서 빠른 검색, Chrome 브라우저를 통한 새로운 윈도우에서 빠른 검색

<br>

## 사용 방법

1. `Alfred` 실행
2. 키워드 + 스페이스바 + 매개변수로 입력 (매개 변수가 있는 경우)
3. 키워드만 입력 (매개 변수가 없는 경우)

![Nov-14-2024 23-32-14](https://github.com/user-attachments/assets/743189c9-4af3-472d-a04c-65fab82e7d75)

<br>

## 사용 가능한 키워드

- Workflows에서 확인해보자. 마우스 스크롤로 위 아래 탐색 할 수 있고, Shift를 누른 채로 마우스 스크롤을 사용하면 좌 우 탐색을 할 수 있다. 마우스 패드로도 빠르게 탐색할 수 있다.
- 맨 왼쪽부터 Whale에서 사용할 수 있는 빠른 검색, Chrome에서 사용할 수 있는 빠른 검색, 개발자 공식 문서 빠른 검색이다.

## 필요한 라이브러리
- jq : 리눅스에서 JSON 데이터 가공하기 위한 라이브러리
```
brew install jq
```

<br>

## 구성

### Alfred Workflows 구성
- 확장이 어려운 구조로 구성되어 있다. 시간을 두고 가지고 놀면서 블록을 최적화 해야한다.
![image](https://github.com/user-attachments/assets/5c312c66-70d7-403a-9282-73cb1374cf51)

<br>

### [script/search/urls.json](https://github.com/Daeho-Son/custom-web-search/blob/main/script/search/urls.json)
- 빠른 검색을 위한 사이트 정보가 JSON 형태로 구성되어 있다.
- `value`는 `base`와 `query`로 구성되어 있다.
- `base`는 홈페이지 url이, `query`는 해당 사이트를 통해 빠른 검색을 하기 위한 url이 설정되어 있다.
- `jq 라이브러리`를 사용해서 데이터를 가공한다.

<br>

### script/search/browser_search.sh
- 브라우저를 통한 빠른 검색을 위한 스크립트이다.

<br>

### script/search/site_search.sh
- 특정 사이트를 통한 빠른 검색을 위한 스크립트이다.

<br>

### script/search/utils/code_point_parser.sh 와 script/search/utils/percent_encoding_parser.py
- 이상하게도 `Alfred Workflow`에서 스크립트를 통해 한글로 검색을 하면 특정 사이트에서 제대로 인식하지 못 하는 퍼센트 인코딩으로 변환되어 한글을 인식하지 못 하는 문제가 있었고, 이걸 해결하기 위해 만든 스크립트이다.

- 정확하게는 `Alfred Workflow`에서 스크립트로 들어오는 한글 유니코드 블록이 [Hangul Jamo](https://en.wikipedia.org/wiki/Hangul_Jamo_(Unicode_block))이기 때문에 발생하는 문제였다.

- 특정 사이트들(예를 들어, 다나와 쇼핑)은 `Hangul Jamo`로 퍼센트 인코딩이 되면 제대로 인식하지 못 했기 때문에, 입력 받은 매개변수를 [Hangul Syllables](https://en.wikipedia.org/wiki/Hangul_Syllables)로 변환해서 제대로 검색될 수 있도록 처리를 했다.

- `컴퓨터`의 유니코드 블록별 차이
  - `Hangul Jamo`로 표기하면 `%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%B2%E1%84%90%E1%85%A5`가 된다.
  - `Hangul Syllables`로 표기하면 `%EC%BB%B4%ED%93%A8%ED%84%B0`가 된다.

- 아래는 구글 사이트에서 `Hangul Jamo` 유니코드 블록으로 검색 (정상적으로 검색됨)
  ![image](https://github.com/user-attachments/assets/8a06b69b-0eb1-4d18-ae63-1905b040541b)

- 아래는 다나와 사이트에서 `Hangul Jamo` 유니코드 블록으로 검색 (검색되지 않음)
  ![image](https://github.com/user-attachments/assets/10c04918-390d-4405-a377-88bfc3146ba2)

- 아래는 다나와 사이트에서 `Hangul Syllables` 유니코드 블록으로 검색 (정상적으로 검색됨)
  ![image](https://github.com/user-attachments/assets/e0117d20-3ebb-40c9-a8b7-799be2a0b6c9)


