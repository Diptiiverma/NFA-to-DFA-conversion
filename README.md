#NFA to DFA Conversion in Python

This project implements a converter that transforms a Non-deterministic Finite Automaton (NFA) — including ε (epsilon) transitions — into its equivalent Deterministic Finite Automaton (DFA) using Python. This is a fundamental concept in automata theory, often used in the design of compilers and lexical analyzers.

⚠️ Note: This implementation considers ε-transitions only for epsilon closure calculation during the conversion process.
It does not support NFA transitions on epsilon as input symbols in the alphabet. That is, ε should not be provided as part of the input alphabet.

✨ Features
`Handles epsilon (ε) transitions for closure.
`Implements subset construction for conversion.
`Computes epsilon-closure of NFA states.
`Identifies final states in the resulting DFA.
`Clearly displays DFA transitions and structure.

🧠 Code Overview
The NFAtoDFA class:
1._init__(): Initializes NFA components.
2.epsilon_closure(states): Finds all states reachable using ε-transitions.
3.move(states, symbol): Finds all states reachable on a specific symbol.
4.convert(): Uses epsilon closures and subset construction to build the DFA.
5.display_dfa(): Outputs all DFA states, transitions, and final states.






