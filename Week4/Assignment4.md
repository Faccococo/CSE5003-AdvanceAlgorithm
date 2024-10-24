---
transition: slide-left
layout: cover
---


# Assignment4
- Zitong Huang, 12432670, Computer Science and Engineering
- 3d Gaussian Splatting for Scene Reconstruction
- Prof. Feng Zheng

---
layout: two-cols
---
# Task 4-1

- Example 1:

Input: 2 machines and 3 jobs: $(t_j = 1, 2, 3)$

$T^* = 3$


- Load Order $(t_j = 1, 2, 3)$, $T = 4$
- Load Order $(t_j = 1, 3, 2)$, $T = 3$
- Load Order $(t_j = 2, 1, 3)$, $T = 4$
- Load Order $(t_j = 2, 3, 1)$, $T = 3$
- Load Order $(t_j = 3, 2, 1)$, $T = 3$
- Load Order $(t_j = 3, 1, 2)$, $T = 3$

$T_{average} = 3.33$

$T_{average} / T^* = 1.11$

::right::
<br></br>
- Example 2:

**Input**: 3 machines and 7 jobs: $(t_j = 1, 1, 1, 1, 1, 1, 3)$, $T^* = 3$

Ignore order of job with load 1

- Load Order $(t_j = 3, 1, 1, 1, 1, 1, 1)$, $T = 3$
- Load Order $(t_j = 1, 3, 1, 1, 1, 1, 1)$, $T = 3$
- Load Order $(t_j = 1, 1, 3, 1, 1, 1, 1)$, $T = 3$
- Load Order $(t_j = 1, 1, 1, 3, 1, 1, 1)$, $T = 4$
- Load Order $(t_j = 1, 1, 1, 1, 3, 1, 1)$, $T = 4$
- Load Order $(t_j = 1, 1, 1, 1, 1, 3, 1)$, $T = 4$
- Load Order $(t_j = 1, 1, 1, 1, 1, 1, 3)$, $T = 5$

$T_{average} = 3.7, T_{average} / T^* = 1.23$

---

# Task 4-2

- Example 1:

**Input**: 3 machines and 7 jobs: $(t_j = 1, 1, 1, 1, 1, 1, 3)$, $T^* = 3$


- From the previous example, $T_{average} = 3.7, and T_{best} will happen when the job with load 3 is assigned to machine **without any task**.

- In sorted order, the job with load 3 is the first job, which will **always be assigned** to the first machine, which means $T_{Sorted} = 3$.

- Thus, $T_{average} / T_{Sorted} = T_{average} / T^* = 1.23$

