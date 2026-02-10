## Overview
This case study documents mutation testing performed on the **Haralick descriptor implementation** from the open-source repository:

👉 https://github.com/TheAlgorithms/Python  
👉 Target file: `computer_vision/haralick_descriptors.py`

The goal was to evaluate test suite effectiveness, identify surviving mutants, and determine where additional assertions or test cases would improve reliability.

This work demonstrates how mutation analysis can guide targeted test design and reliability improvements beyond traditional coverage metrics.

---

## Objective
- Measure mutation adequacy of the existing test suite  
- Identify equivalent vs. non-equivalent surviving mutants  
- Discover missing invariants and boundary-case coverage gaps  
- Propose high-leverage test improvements  

---

## Tooling
- Mutation Engine: **mutmut**
- Test Framework: **pytest**
- Language: Python 3.11
- Key Dependencies: NumPy, ImageIO

Full environment dependencies are provided in: config/requirements.txt


---

## Methodology
1. Generated mutants using mutmut AST mutation engine  
2. Executed pytest test suite against each mutant  
3. Classified mutants as:
   - **Killed** — test suite detected behavioral change  
   - **Survived** — test suite did not detect mutation  
4. Analyzed surviving mutants to identify:
   - Equivalent mutations  
   - Missing assertions  
   - Missing case partitions  
   - Untested control-flow paths  

---

## Results Summary
| Metric | Value |
|---|---|
| Total Mutants | 290 |
| Killed | 211 |
| Equivalent | 19 |
| Effectiveness | ~77.9% |

Mutation effectiveness was strongest in numeric helper routines and weakest in image/matrix iteration logic.

---

## Key Findings
- Numeric routines were well protected by output-based assertions  
- Image and matrix iteration code benefited most from **small, exact fixtures**  
- Several surviving mutants revealed missing **type, shape, and invariant checks**  
- A small number of well-placed invariant assertions could eliminate multiple survivors simultaneously  

---

## Engineering Takeaways

- **Mutation testing exposes gaps traditional coverage misses.**  
  Many surviving mutants preserved final outputs while violating intermediate invariants, showing that coverage alone is not a reliable proxy for test effectiveness.

- **Small, deterministic fixtures outperform large real-world inputs for correctness validation.**  
  Tiny, fully specified matrices and images were significantly more effective at detecting off-by-one, loop-bound, and neighborhood-definition errors.

- **Invariant-based assertions provide the highest return on test investment.**  
  A small number of well-placed type, shape, and invariant checks can eliminate multiple classes of surviving mutants simultaneously.

---

## Repository Artifacts

### Results

Contains:
- Survived / killed classification
- Full mutation diffs
- Raw mutation reports

Full academic report available in:
results/mutation_adequacy_report_haralick_descriptors.pdf

### Configuration

Contains:
- Python dependency environment
- Historical mutation tool configuration

### Added Tests

Contains:
- Targeted tests designed to eliminate non-equivalent survivors

---

## Reproducibility Notes
This repository **does not include upstream source code**.

To reproduce:
1. Clone TheAlgorithms repository  
2. Install dependencies from `config/requirements.txt`  
3. Run mutation testing using mutmut  

---

## Why Mutation Testing Here?
Traditional correctness tests verified output values but did not always constrain:
- Loop bounds  
- Matrix neighborhood definitions  
- Intermediate computation correctness  

Mutation testing exposed these hidden gaps.

---

## Future Improvements
- Add invariant assertion helpers for matrix/image routines  
- Introduce more tiny, fully-specified image fixtures  
- Automate mutation result aggregation and reporting  
- Integrate mutation testing into CI workflow

---

## Upstream Credit
All algorithm implementations belong to:
TheAlgorithms Contributors  
https://github.com/TheAlgorithms/Python