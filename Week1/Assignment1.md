---
transition: slide-left
---

# Assigment1

- Zitong Huang, 12432670, Computer Science and Engineering
- 3d Gaussian Splatting for Scene Reconstruction
- Prof. Feng Zheng

---
layout: cover
---

# TSP

--- 
layout: default
---

- Fix Start City:

TSP ask for visit all city, so we can assum every path start from one（since every path should pass by this city）.

- All Path: 

There are $(n - 1)!$ ways to arrange the remaining $n−1$ cities. This represents all possible sequences of visiting the cities.

- Flip path

Consider two flip path are same, result should devided by 2.

- **Answer:**

An n-city Traveling Salesman Problem has 
$$\dfrac{(n - 1)!}{2}$$
different routes. 

---
layout: cover
---

# Load Balancing(4-job)


---
layout: two-cols
---

**Approach:**

1. **All possible job partitions**
   - Since machines are identical, consider unordered partitions of the total jobs (4) into up to 3 non-negative integers.
     - [4, 0, 0]
     - [3, 1, 0]
     - [2, 2, 0]
     - [2, 1, 1]

**Answer:**

- For summary, total num is 1+4+3+6=14
::right::

2. **Calculate:**

   - **Partition [4, 0, 0]:**
     - only **1 unique assignment**.

   - **Partition [3, 1, 0]:**
     - $\binom{4}{3} = 4$.

   - **Partition [2, 2, 0]:**
     - $\binom{4}{2} / 2 = 3$

   - **Partition [2, 1, 1]:**
     - $\binom{4}{2} = 6$

--- 
layout: cover
---

# Load Balancing (n-job)

---
layout: default
---

### **Approach:**

- Total number of possible assignments is $2^n$.

- Machines are identical, swapping the assignments between machines doesn't yield a new solution, so total num should be devided by 2.


### **Answer:**

**For 2 identical machines and n distinct jobs, there are $\mathbf{2^{n-1}}$ different solutions.**

---
layout: cover
---

# 30-Item-Knapsack

---
layout: default
---

**Keypoints**:

1. choices are independent
> solutions includes the selection of **no items** and the selection of **all
items**.

2. Each item have **2** state

> 0: not selected, 1: selected

<br></br>

## Answer:

The total number of possible solutions is $2^{30}$.
