---
transition: slide-left
---

#    NSGA-II:
<span style="font-size: 2.0rem;">IPPS Solution of Large-Size Valve Production in *Yuanda*</span>

- Zitong Huang, 12432670
- Department of Computer Science and Engineering
- Scene Reconstruction
- Prof. Feng Zheng

---

# Content

1. Multi-Objective Optimization

2. Integrated Process Planning and Scheduling

3. NSGA-II Algorithm

4. Application: Machining Job Shop for Large-size Valve

---
layout: two-cols
---

## Multi-Objective Optimization 
A multi-objective optimization problem can be expressed as:

$$
\begin{align*}
\text{Minimize} & \quad \mathbf{f}(x) = \begin{pmatrix} f_1(x) \\ f_2(x) \\ \vdots \\ f_k(x) \end{pmatrix} \\
\text{Subject to} & \quad x \in X
\end{align*}
$$

Here:

- $x$ is the decision vector within the feasible set $X \subseteq \mathbb{R}^n$.
- $\mathbf{f}(x)$ is a vector of $k$ objective functions $f_i(x)$ to be minimized.

::right::

**Pareto Optimality:**

In multi-objective optimization, the focus is on Pareto optimal solutions where improving one objective worsens another(due to their conflicting nature).

A solution $x^*$ is Pareto optimal if there is no other solution $x \in X$ such that:

$$
\begin{cases}
f_i(x) \leq f_i(x^*) & \text{for all } i \in \{1, \dots, k\} \\
f_j(x) < f_j(x^*) & \text{for at least one } j
\end{cases}
$$

The set of all Pareto optimal solutions forms the Pareto front, representing the trade-offs between different objectives.

---
layout: two-cols
---

## Integrated Process Planning and Scheduling (IPPS)

Integrated Process Planning and Scheduling (IPPS) is the simultaneous optimization of process planning and production scheduling to improve manufacturing efficiency:

**Sets:**
- $J$: Set of jobs.
- $M$: Set of machines.
- $O_j$: Set of operations for job $j \in J$.
- $P_{o}$: Set of alternative process plans for operation $o \in O_j$.

::right::

**Parameters:**
- $p_{o,m}$: Processing time of operation $o$ on machine $m$.
- $s_{o,o'}$: Sequence-dependent setup time between operations $o$ and $o'$.
- $\text{ST}_{o,o'}$: Binary parameter indicating if operation $o$ must precede operation $o'$ (1 if true, 0 otherwise).

**Decision Variables:**
- $x_{o,m}$: Binary variable equal to 1 if operation $o$ is assigned to machine $m$; 0 otherwise.
- $C_o$: Completion time of operation $o$.
- $S_o$: Start time of operation $o$.

---
layout: two-cols
---

## Integrated Process Planning and Scheduling (IPPS) Contd.

**Objective Function:**

1. **Minimizing Manufacturing Time and Costs**:
  $$
   \text{Minimize } f_1 = f_2 + f_3
  $$
   - $f_2$: maximum time required to complete all tasks across machines.
   - $f_3$: Manufacturing costs

2. **Makespan Minimization**:
  $$
   f_2 = \text{min } T = \text{min } (MT + LT)
  $$
   - $MT$: Maximum machining time
   - $LT$: Loading and unloading time

::right::
3. **Manufacturing Costs Minimization**:
  $$
   f_3 = \text{min } C = \text{min } (MC + TC + MTC)
  $$
   where:
   - $MC$: Total machining cost.
   - $TC$: Tool cost for machining.
   - $MTC$: Machine conversion cost (cost incurred when transferring a job between machines).

Additionally, a conversion factor, $\alpha(M_i, M_j)$, is used to account for the time spent in loading and unloading parts between machines.

$$
\alpha(M_i, M_j) =
\begin{cases} 
1 & \text{if } M_i \neq M_j \\
0 & \text{if } M_i = M_j
\end{cases}
$$


---

# NSGA II

The method relies on **NSGA-II**, a genetic algorithm that uses a population of solutions and evolves them over generations. Here are the key features of the algorithm:

1. **Two-Section Encoding**: 
   - The encoding of a solution consists of two parts:
     - **Operation Sequence (OS)**: The order in which operations are performed.
     - **Machine Assignment (MA)**: The machine assigned to each operation.
   
2. **Crossover and Mutation**:
   - The **PMX (Partially Mapped Crossover)** is used for the operation sequence.
   - **Random mutation** changes the operation order and machine assignments to explore new solutions.

---

# NSGA II Contd.


3. **Elite Strategy**:
   - It includes a **dynamic population update** that removes duplicate solutions and an **adaptive mutation** that adjusts mutation rates based on entropy to avoid local optima.

4. **Fitness Evaluation**:
   - The fitness of each solution is evaluated using the makespan and manufacturing costs, with a fast non-dominated sorting approach used to rank solutions.

---

## Application: Machining Job Shop for Large-size Valve in Yuanda Valve Company

<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
>Wang J, Xu L, Sun S, Ma Y, Yu G (2024) Multi-objective optimization using improved NSGA-II for integrated process planning and scheduling problems in a machining job shop for large-size valve. PLoS ONE 19(6): e0306024. https://doi.org/10.1371/journal.pone.0306024
