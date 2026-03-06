# Algorithm Solving

BOJ와 SWEA 문제 풀이 기록을 정리한 저장소입니다.  
학습 경로에 따라 문제를 구분하여 관리합니다.

---

## Repository Structure
```text
algorithm-solving
├ course       # 수업 및 실습 문제 (기존 학습 흐름 유지)
│ └ MMDD_type  # SWEA 문제 (수업 유형 기준)
│
├ personal     # 개인적으로 풀이하며 유형별로 정리한 문제
│ ├ BOJ
│ │ └ type
│ └ SWEA
│   └ type
│
└ study        # 스터디에서 풀이한 문제
  └ MMDD
```

### Structure Rule
- **BOJ 문제**
  - 폴더 안에 바로 `.py` 파일이 위치합니다.

- **SWEA 문제**
  - 폴더 안에 `문제번호 폴더`가 생성됩니다.
  - 해당 폴더 안에 `input / output / .py` 파일이 포함됩니다.

### Example
```text
study
└ 0115
  ├ 1234.py          # BOJ
  └ 1208
    ├ input.txt
    ├ output.txt
    └ 1208.py        # SWEA
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
- Python