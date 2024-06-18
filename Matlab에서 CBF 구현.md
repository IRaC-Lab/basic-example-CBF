#Programming #ControlTheory 

## Environment
---
- Matlab 2024a
- Simulink
- Simulink Control Design
- Control System Toolbox

## Method
---
- Simulink block 중 Barrier Certificate Enforcement 사용
- [[CBF 기본개념]]에서 QP 문제를 풀 수 있음
- Block 에서의 QP 문제 표현식
	- $u^* = \min_{u} ||u - u_0||^2 ~~ s.t. ~~ q_xf_x + q_xg_xu + \gamma h_x^\beta \leq 0$
	- 입력 제한 가능: $u_{min} \geq u \geq u_{max}$
- System이 $\dot{x} = f(x) + g(x)u$ 일때 block에 입력하는 parameter
	- $u_0$: 추종하려는 제어입력(nominal controller)
	- $f_x$: $f(x)$
	- $g_x$: $g(x)$
	- $q_x$: $\frac{dh(x)}{dt}$
	- $h_x$: $h(x)$
- 출력 parameter: $u^*$

## 관련메모
---
- [[Matlab 강의 정리]]

## 참고문헌
---
- https://kr.mathworks.com/help/releases/R2024a/slcontrol/constraint-enforcement.html?lang=en