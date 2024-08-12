---
tags:
  - Matlab
  - Programming
---
- OS
	- Mac OS

## 터미널에서 설정
- 파이썬 설치 확인
```bash
/usr/bin/python3 --version
```

- 파이썬 가상환경 생성
```bash
/usr/bin/python3 -m venv /home/username/cbf_venv
```

- 가상환경 활성화
```bash
source /home/username/cvf_venv/bin/activate
```

- 패키지 설치
```bash
pip install cvxpy
```

 - 패키지 설치 확인
```bash
python
>>> import cvxpy
```

- 파이썬 실행파일 위치 찾기
```bash
>>> import sys
>>> sys.excutable
```

```bash
/Users/bumyong/Library/CloudStorage/Dropbox/1_Work/1_Projects/CBF/cbf_venv/bin/python
```
## Matlab에서 설정

- 파이썬 환경 설정
```matlab
pyenv('Version', '파이썬 실행파일 위치')
```

- 모듈 실행 확인
```matlab
py.importlib.import_module('cvxpy')
```
