---
transition: slide-left
layout: cover
---

# Assignment10 : Vertex Cover Problem
- Zitong Huang, 12432670, Computer Science and Engineering
- Scene Reconstruction
- Prof. Feng Zheng

---
layout: two-cols
---

# Task 10-1

$$
\text{Target: } \max Z = \mathbf{c}^T \mathbf{x} = [-1,\ 2] \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$

$$
\text{Subject to: } 
\begin{bmatrix} 
3 & 2 \\ 
-1 & 1

\end{bmatrix}
\begin{bmatrix} 
x_1 \\ 
x_2 
\end{bmatrix}
\leq 
\begin{bmatrix} 
4 \\ 
1  
\end{bmatrix},\quad x_1, x_2 \geq 0
$$


<br></br>
<br></br>
<br></br>

| Algorithm | $x_1$  | $x_2$  |   Z    |
|-----------|--------|--------|--------|
|HiGHS$^{[1]}$   | 0.4    |  1.4   | 2.4    |
|Simplex$^{[2]}$   | 0.4    | 1.4    | 2.4    |
::right::

<div align="center">
    <img src="./img/image.png" width="60%">
</div>

<br></br>


>[1] Huangfu, Q., & Hall,  J. J. (2018). Parallelizing  the dual revised  simplex method. Mathematical  Programming  Computation,  10(1), 119-142.
>
>[2] Dantzig, G. B. (1948). Programming in a linear structure. Econometrica, 17(1), 73–74.

---
layout: two-cols
---

# Task 10-1

$$
\text{Target: } \max Z = \mathbf{c}^T \mathbf{x} = [2,\ 1] \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$

$$
\text{Subject to: } 
\begin{bmatrix} 
2 & 1 \\ 
-2 & 2 \\
0 & -1
\end{bmatrix}
\begin{bmatrix} 
x_1 \\ 
x_2 
\end{bmatrix}
\leq 
\begin{bmatrix} 
4 \\ 
-1 \\
0  
\end{bmatrix},\quad x_1, x_2 \geq 0
$$

<br></br>
<br></br>
<br></br>

| Algorithm | $x_1$  | $x_2$  |   Z    |
|-----------|--------|--------|--------|
|HiGHS$^{[1]}$   | 2    |  0   | 4    |
|Simplex$^{[2]}$   | 2    | 0    | 4    |
::right::

<div align="center">
    <img src="./img/image copy.png" width="80%">
</div>
<br></br>


>[1] Huangfu, Q., & Hall,  J. J. (2018). Parallelizing  the dual revised  simplex method. Mathematical  Programming  Computation,  10(1), 119-142.
>
>[2] Dantzig, G. B. (1948). Programming in a linear structure. Econometrica, 17(1), 73–74.

---
layout: two-cols
---
# Task 10-1

$$
\max Z = \mathbf{c}^T \mathbf{x} = [1,\ 2,\ 3] \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \\
\text{Subject to: }
\begin{bmatrix}
    1 & 2 & 3 \\
    2 & 1 & 1 \\
    1 & 1 & 2 \\
    -1 & 0 & 0 \\
    0 & -1 & 0 \\
    0 & 0 & -1

\end{bmatrix}
\begin{bmatrix}
    x_1 \\
    x_2 \\
    x_3
\end{bmatrix}
\leq
\begin{bmatrix}
    6 \\
    4 \\
    5 \\
    0 \\
    0 \\
    0
\end{bmatrix}
$$

| Algorithm      | $x_1$  | $x_2$  | $x_3$  |   Z    |
|----------------|--------|--------|--------|--------|
|HiGHS$^{[1]}$   |  0   |  0   |   2     |  6   |
|Simplex$^{[2]}$ |  0   |  0   |   2     |  6   |

::right::

<div align="center">
    <img src="./img/image copy 2.png" width="80%">
</div>

<br></br>

>[1] Huangfu, Q., & Hall,  J. J. (2018). Parallelizing  the dual revised  simplex method. Mathematical  Programming  Computation,  10(1), 119-142.
>
>[2] Dantzig, G. B. (1948). Programming in a linear structure. Econometrica, 17(1), 73–74.

---

# Task 10-2

<br> </br>

| Instances | HiGHS time (s)       | HiGHS optimal       | Interior-Point$^{[1]}$ time (s)       | Interior-Point optimal       |
|-----------|----------------------|---------------------|---------------------|--------------------|
| small     | 0.0012        | 8106.530114360896   | 0.008       | 8106.530114300792  |
| medium    | 2.5243         | 5653427.100619743   | 1.5281        | 5653427.098690189     |
| large     | 69.2118         | 54087865.84468825   | 58.5074        |  Failed to Solve     |

> [1] Dikin, I. I. (1967). Iterative solution of problems of linear and quadratic programming. Doklady Akademii Nauk SSSR, 174(4), 747–748.