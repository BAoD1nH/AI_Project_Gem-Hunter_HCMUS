# 💎 Gem Hunter: AI Agent with CNF Solving

**Gem Hunter** is an AI-driven project featuring an intelligent agent designed to navigate a 2D grid world. The agent's primary objective is to collect gold while successfully identifying and avoiding hidden traps by applying logical reasoning through **CNF (Conjunctive Normal Form)** solving algorithms.

## 🌟 Core Concept
In this environment, the agent operates under "partial observability." It does not know the location of traps or gold initially but perceives "hints" (percepts) from adjacent cells. By converting these hints into logical clauses, the agent builds a **Knowledge Base (KB)** and uses a SAT solver to deduce safe paths.



## 🧠 Logic & Algorithm: CNF Solving
The project implements logical deduction by representing the world's rules as a series of boolean variables and clauses:

1.  **Logical Representation**: Each cell $(x, y)$ is represented by propositions such as $T_{x,y}$ (Trap) or $G_{x,y}$ (Gold).
2.  **CNF Conversion**: Rules like *"If a cell has a breeze, at least one adjacent cell must contain a trap"* are converted into CNF.
    * *Example:* $(B_{1,1} \implies T_{1,2} \lor T_{2,1})$ becomes $(\neg B_{1,1} \lor T_{1,2} \lor T_{2,1})$.
3.  **Resolution/SAT Solving**: The agent queries its Knowledge Base to check if a move is "Provably Safe" by attempting to prove that a trap cannot exist in the target cell.



## 🛠 Features
* **Dynamic Knowledge Base**: Updates in real-time as the agent explores new cells.
* **CNF Solver Integration**: Efficiently handles logical constraints to ensure zero-fatality navigation.
* **2D Map Visualization**: Clear UI/Terminal display showing the agent's path, current knowledge, and discovered items.
* **Customizable Maps**: Support for different grid sizes and trap densities.
