---
transition: slide-left
layout: cover
---


# Assignment3
- Zitong Huang, 12432670, Computer Science and Engineering
- 3d Gaussian Splatting for Scene Reconstruction
- Prof. Feng Zheng

---

# Task 3-1



## Example:  $5$ Machine and $3$ Jobs
- $N(Machinese) = 5$
- Jobs: $t_i$ = {3, 1, 2}
   

## Example: $6$ Machine and $4$ Jobs

- $N(Machine) = 3$
- Jobs: $t_i$ = {1, 6, 2, 5}

---
layout: two-cols-header
---

# Task 3-2: Example 1

- $N(Machine) = 3$
- Jobs: $t_i$ = {1, 2, 5, 6}

## Example:
::left::
- allocate order ${t_1, t_2, t_3, t_4}$:
1. allocate $t_1 = 1$ to machine 1. **$Load$**: {1, 0, 0}
2. allocate $t_2 = 2$ to machine 2. **$Load$**: {1, 2, 0}
3. allocate $t_3 = 5$ to machine 3. **$Load$**: {1, 2, 5}
4. allocate $t_4 = 6$ to machine 1. **$Load$**: {7, 2, 5}

Maximum load: $7$

**Order of allocation affects the final load of each machine.**

::right::
- allocate order ${t_4, t_3, t_2, t_1}$:
1. allocate $t_4$ to machine 1. **$Load$**: {6, 0, 0}
2. allocate $t_3$ to machine 2. **$Load$**: {6, 5, 0}
3. allocate $t_2$ to machine 3. **$Load$**: {6, 5, 2}
4. allocate $t_1$ to machine 3. **$Load$**: {6, 5, 3}

Maximum load: $6$

---
layout: two-cols-header
---

# Task 3-2: Example 2
- $N(Machine) = 3$
- Jobs: $t_i$ = {5, 5, 5, 5, 10}

## Example:

::left::
- allocate order ${t_1, t_2, t_3, t_4, t_5}$:
1. allocate $t_1 = 5$ to machine 1. **$Load$**: {5, 0, 0}
2. allocate $t_2 = 5$ to machine 2. **$Load$**: {5, 5, 0}
3. allocate $t_3 = 5$ to machine 3. **$Load$**: {5, 5, 5}
4. allocate $t_4 = 5$ to machine 1. **$Load$**: {10, 5, 5}
5. allocate $t_5 = 10$ to machine 2. **$Load$**: {10, 15, 5}

Maximum load: $15$

::right::
- allocate order ${t_5, t_4, t_3, t_2, t_1}$:
1. allocate $t_5 = 10$ to machine 1. **$Load$**: {10, 0, 0}
2. allocate $t_4 = 5$ to machine 2. **$Load$**: {10, 5, 0}
3. allocate $t_3 = 5$ to machine 3. **$Load$**: {10, 5, 5}
4. allocate $t_2 = 5$ to machine 2. **$Load$**: {10, 10, 5}
5. allocate $t_1 = 5$ to machine 3. **$Load$**: {10, 10, 10}

Maximum load: $10$


---

# Task 3-3: $2$ Machine and $3$ Jobs

- Proof:
    - Assume $t_i$ = {a, b, c}, where $a > b > c$
    - Worst case of greedy algorithm: $T_{worst} = max(a, b, c) + min(b, c) = a + c$
    - Optimal solution: $T = max(a, b + c)$
    - We have 
    $$
    \begin{aligned}
    \begin{equation}
        \frac{T}{T^*} = 
        \begin{cases} 
            a / (a+c) & \text{if} (a \geq b + c )\\
            (b+c) / (a+c) & \text{if }( a < b + c)
        \end{cases}
    \end{equation}
    \end{aligned}
    $$

    Simplify, we have $\frac{T}{T^*} >= \frac{2}{3}$

- Example:
    - $t_i$ = {10, 5, 5}
    - **Greedy algorithm:** $T_{worst} = 15$, **Optimal solution**: $T* = 10$


---

# Task 3-3: $4$ Machine and $7$ Jobs

- Example: 
    - $t_i$ = {10, 10, 10, 10, 10, 10, 30}
    - $T_{worst}: {20, 20, 50} = 50$
    - $T*: {30, 30, 30} = 30$


---

# Task 3-3: $m$ Machine and $n$ Jobs

- Assume $t_i$ = {t_1, t_2, ..., t_n}, where $t_1 \geq t_2 \geq ... \geq t_n$, and $n \gg m$

- Worst case of greedy algorithm: $T_{worst} = t_1 + min_{S_{n-1}}$, since minimum value in solution of $T_{n-1} = (t_2, t_3, ..., t_n)$ on $m$ machine **satisfied** $min_{S_{n-1}} \leq \frac{sum(t_2, t_3, ..., t_n)}{m}$

- Optimal solution: $T^*\geq \frac{sum(t_1, t_2, t_3, ..., t_n)}{m}$

We have $\frac{T_{worst}}{T^*}$ = $\frac{t_1 + S_{n-1}}{T^*}$
- For some spetial cases that  $t_1 = \frac{sum(t_2, ..., t_n)}{(m-1)}$(like examples above), $T^* = \frac{sum(t_1, t_2, t_3, ..., t_n)}{m} = t_1$, $T_{worst} = t_1 + min_{S_{n-1}} \geq t_1 + \frac{sum(t_2, t_3, ..., t_n)}{m}$, We have:

$$
Ratio_{max} = \frac{t_1 + \frac{sum(t_2, t_3, ..., t_n)}{m}}{t_1} = \frac{t_1 + \frac{(m - 1)t_1}{m}}{t_1} = \frac{2m-1}{m} \to 2 (when\space m \to \infty)
$$

Thus, when $t_1 = \frac{sum(t_2, ..., t_n)}{m-1}$, and  the ratio is maximum close to 2.




