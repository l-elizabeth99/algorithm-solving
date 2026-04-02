# Algorithm Solving

BOJ와 SWEA 문제 풀이 기록을 정리한 저장소입니다.  
학습 경로에 따라 문제를 구분하여 관리합니다.  
이전 풀이는 Python을,  
새로운 풀이는 java를 사용합니다.  

---

## Repository Structure
```text
algorithm-solving
├ course
│ └ MMDD_type
│
├ personal
│ ├ BOJ
│ │ └ type
│ └ SWEA
│   └ type
│
└ study
  └ MMDD
```

### Structure Rule
- **파일명**
  - python의 경우 `문제번호.py`로,
  - java의 경우 `P문제번호.java`로 통일합니다. (Java 클래스 명명 규칙 준수)

- **BOJ 문제**
  - 폴더 안에 바로 `.py` 혹은 `.java` 파일이 위치합니다.

- **SWEA 문제**
  - 폴더 안에 `문제번호 폴더`가 존재하고,
  - 해당 폴더 안에 `input / output / .py or .java` 파일이 위치합니다.

- **course 폴더**
  - 수업 및 실습에서 풀이한 문제 폴더입니다.
  - 기존 학습 흐름을 그대로 유지하여 SWEA 문제만 존재합니다.
  - 해당 폴더 안에 규칙에 따른 `.py` 파일이 위치합니다.
  
- **study 폴더**
  - 스터디에서 풀이한 문제 폴더입니다.
  - 기존 스터디 흐름을 유지하여 SWEA 문제와 BOJ 문제가 공존합니다.
  - 해당 폴더 안에 규칙에 따른 `.py` 파일이 위치합니다.
  
- **personal 폴더**
  - java 언어를 사용해 개인적으로 풀이한 문제 폴더입니다.
  - SWEA 문제와 BOJ 문제가 공존합니다.
  - 해당 폴더 안에 규칙에 따른 `.java` 파일이 위치합니다.

### Example
```text
study
└ 0115
  ├ 1234.py          # BOJ
  └ 1208
    ├ input.txt
    ├ output.txt
    └ 1208.py        # SWEA

personal
└ BOJ
  └ 반복문
    └ P10828.java
└ SWEA
  └ 1208
    ├ input.txt
    └ P1208.java
```

---

## Platforms
- **BOJ** (Baekjoon Online Judge)
- **SWEA** (Samsung SW Expert Academy)

---

## Purpose
- 알고리즘 문제 풀이 기록 관리
- 유형별 문제 정리 및 복습
- 풀이 과정 정리

---

## Language
<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python">
  <img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" alt="java">
</p>
