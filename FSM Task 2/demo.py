class Transition:
    """A change from one state to a next"""

    def __init__(self, current_state, state_input, next_state):
        self.current_state = current_state
        self.state_input = state_input
        self.next_state = next_state

    def match(self, current_state, state_input):
        """Determines if the state and the input satisfies this transition relation"""
        return self.current_state == current_state and self.state_input == state_input

class FSM:
    """A basic model of computation"""

    def __init__(
            self,
            states=[],
            alphabet=[],
            accepting_states=[],
            initial_state=''):
        self.states = states
        self.alphabet = alphabet
        self.accepting_states = accepting_states
        self.initial_state = initial_state
        self.valid_transitions = False

    def add_transitions(self, transitions=[]):
        """Before we use a list of transitions, verify they only apply to our states"""
        for transition in transitions:
            if transition.current_state not in self.states:
                print(
                    'Invalid transition. {} is not a valid state'.format(
                        transition.current_state))
                return
            if transition.next_state not in self.states:
                print('Invalid transition. {} is not a valid state'.format)
                return
        self.transitions = transitions
        self.valid_transitions = True

    def __accept(self, current_state, state_input):
        """Looks to see if the input for the given state matches a transition rule"""
        # If the input is valid in our alphabet
        if state_input in self.alphabet:
            for rule in self.transitions:
                if rule.match(current_state, state_input):
                    return rule.next_state
            print('No transition for state and input')
            return None
        return None

    def accepts(self, sequence):
        """Process an input stream to determine if the FSM will accept it"""
        # Check if we have transitions
        if not self.valid_transitions:
            print('Cannot process sequence without valid transitions')

        print('Starting at {}'.format(self.initial_state))
        # When an empty sequence provided, we simply check if the initial state
        # is an accepted one
        if len(sequence) == 0:
            return self.initial_state in self.accepting_states

        # Let's process the initial state
        current_state = self.__accept(self.initial_state, sequence[0])
        if current_state is None:
            return False

        # Continue with the rest of the sequence
        for state_input in sequence[1:]:
            print('Current state is {}'.format(current_state))
            current_state = self.__accept(current_state, state_input)
            if current_state is None:
                return False

        print('Ending state is {}'.format(current_state))
        # Check if the state we've transitioned to is an accepting state
        return current_state in self.accepting_states


# Set up our FSM with the required info:
# Set of states
states = ['State 1', 'State 2', 'Error']
# Set of allowed inputs
alphabet = [1, 0]
# Set of accepted states
accepting_states = ['State 1']
# The initial state
initial_state = 'State 1'
fsm = FSM(states, alphabet, accepting_states, initial_state)

# Create the set of transitions
transition1 = Transition('State 1', 1, 'State 2')
transition2 = Transition('State 2', 0, 'State 1')
transition3 = Transition('State 1', 0, 'Error')
transition4 = Transition('State 2', 1, 'Error')
transition5 = Transition('Error', 1, 'Error')
transition6 = Transition('Error', 0, 'Error')
transitions = [
    transition1,
    transition2,
    transition3,
    transition4,
    transition5,
    transition6]
# Verify and add them to the FSM
fsm.add_transitions(transitions)

# Now that our FSM is correctly set up, we can give it input to process
# Let's transition the FSM to a green light
should_be_accepted = fsm.accepts([1, 0, 1, 0])
print(should_be_accepted)

# Let's transition the FSM to a red light
should_be_rejected_1 = fsm.accepts([1, 1, 1, 0])
print(should_be_rejected_1)

# Let's transition to yellow and give it bad input
should_be_rejected_2 = fsm.accepts([1, 0, 1, 0, 1, 0, 0])
print(should_be_rejected_2)
