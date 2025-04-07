from collections import defaultdict

class NFAtoDFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.nfa_states = states
        self.alphabet = alphabet
        self.nfa_transitions = transitions  # {state: {symbol: {next_states}}}
        self.start_state = start_state
        self.final_states = set(final_states)
        
        self.dfa_states = []  # List of DFA states (sets of NFA states)
        self.dfa_transitions = {}  # DFA transition table
        self.dfa_final_states = set()
               
    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        
        while stack:
            state = stack.pop()
            if "" in self.nfa_transitions.get(state, {}):  # epsilon transitions
                for next_state in self.nfa_transitions[state][""]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return frozenset(closure)
    
    def move(self, states, symbol):
        next_states = set()
        for state in states:
            if symbol in self.nfa_transitions.get(state, {}):
                next_states.update(self.nfa_transitions[state][symbol])
        return next_states
    
    def convert(self):
        start_closure = self.epsilon_closure({self.start_state})
        self.dfa_states.append(start_closure)
        state_queue = [start_closure]
        
        while state_queue:
            current_dfa_state = state_queue.pop(0)
            self.dfa_transitions[current_dfa_state] = {}
            
            for symbol in self.alphabet:
                if symbol == "":
                    continue  # Skip epsilon
                move_result = self.move(current_dfa_state, symbol)
                epsilon_closure_result = self.epsilon_closure(move_result)
                
                if epsilon_closure_result not in self.dfa_states:
                    self.dfa_states.append(epsilon_closure_result)
                    state_queue.append(epsilon_closure_result)
                
                self.dfa_transitions[current_dfa_state][symbol] = epsilon_closure_result
                
        for dfa_state in self.dfa_states:
            if self.final_states & dfa_state:
                self.dfa_final_states.add(dfa_state)
    
    def display_dfa(self):
        print("DFA States:")
        for i, state in enumerate(self.dfa_states):
            print(f"Q{i}: {set(state)}")
        
        print("\nDFA Transitions:")
        for state, transitions in self.dfa_transitions.items():
            print(f"State {set(state)}:")
            for symbol, next_state in transitions.items():
                print(f"  {symbol} -> {set(next_state)}")
        
        print("\nDFA Start State:", set(self.dfa_states[0]))
        print("DFA Final States:", [set(state) for state in self.dfa_final_states])

# User Input
num_states = int(input("Enter the total number of states in NFA: "))
nfa_states = {str(i) for i in range(num_states)}

alphabet = set(input("Enter alphabet symbols (space-separated): ").split())
transitions = defaultdict(lambda: defaultdict(set))  

for state in nfa_states:
    for symbol in alphabet:
        num_transitions = int(input(f"Enter the number of transitions for state {state} on input {symbol}: "))
        for i in range(num_transitions):
            next_state = input(f"Enter state for transition {i+1}: ")
            transitions[state][symbol].add(next_state)

start_state = input("Enter start state: ")
num_final_states = int(input("Enter the number of final states: "))
final_states = {input(f"Enter final state {i+1}: ") for i in range(num_final_states)}

nfa_to_dfa = NFAtoDFA(nfa_states, alphabet, transitions, start_state, final_states)
nfa_to_dfa.convert()
nfa_to_dfa.display_dfa()
