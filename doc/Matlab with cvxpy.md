## Motivation
- CBF를 사용한 제어기를 설계하기 위해 QP로 모델링한 문제를 풀 수 있어야함
- Matlab에서 제공하는 Barrier Certificate Enforcement는 Simulink Control Design toolbox가 따로 필요하고 실제 로봇에 적용하기 어려움
- Convex optimization 문제를 모델링 할 수 있는 파이썬 패키지(CVXPY)를 사용해서 QP를 모델링 할 수 있음
- CVXPY를 사용해서 설계한 파이썬 모듈을 검증하기 위해 기존 matalb 시뮬레이션 환경에서 테스트 할 필요가 있음

## Objective
- Simulink에서 python 모듈을 불러와서 사용할 수 있는 환경을 구성하고 테스트
- 기존 CBF 예제에서 Barrier Certificate Enforcement 대신 CVXPY를 사용해서 설계한 파이썬 모듈 사용해서 테스트

## Development Environment
- Matlab
- Python
- [CVXPY](https://www.cvxpy.org/index.html)

## Setup
1. [CVXPY 설치](https://www.cvxpy.org/install/index.html)
2. [CVXPY예제 파이썬 환경에서 테스트](https://www.cvxpy.org/examples/basic/least_squares.html)
3. [Matlab에서 파이썬 가상환경 설정](./Matlab에서%20파이썬%20가상환경%20설정.md)
4. [Matlab에서 파이썬 모듈 사용 테스트](https://kr.mathworks.com/help/matlab/matlab_external/call-user-defined-custom-module.html)
5. [Simulink에서 파이썬 모듈 사용](https://kr.mathworks.com/help/simulink/ug/python_simulink_example.html?searchHighlight=simulink%20python&s_tid=srchtitle_support_results_2_simulink%20python)