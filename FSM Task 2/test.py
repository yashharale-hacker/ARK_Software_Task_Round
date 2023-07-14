# using functions seperately
def print_list_of_juices():
    print("\n\tVending Machine Drinks List")
    print("Sl. No.\t Drink\t\t\t Code\tCost")
    print("1\t\t Pepsi\t\t\t PEPS\t 30")
    print("2\t\t Mountain Dew\t MDEW\t 30")
    print("3\t\t Dr.Pepper\t\t DPEP\t 50")
    print("4\t\t Coke\t\t\t COKE\t 20")
    print("5\t\t Gatorade\t\t GATO\t 20")
    print("6\t\t Diet Coke\t\t DCOK\t 30")
    print("7\t\t Minute Maid\t MINM\t 25")
    print("8\t\t Tropicana\t\t TROP\t 30\n")


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
    """Model fo Finite State Machine"""

    def __init__(self, states=[], inputs_allowed=[], accepting_states=[], initial_state='', no_of_cans=0, COST=[]):
        self.states = states
        self.inputs_allowed = inputs_allowed
        self.accepting_states = accepting_states
        self.initial_state = initial_state
        self.quantity = [no_of_cans * 8, no_of_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans,
                         no_of_cans, no_of_cans]
        self.no_of_cans = no_of_cans
        self.COST = COST
        self.valid_transitions = False

    def add_transitions(self, transitions=[]):
        """Before we use a list of transitions, verifying that they only apply to our states"""
        for transition in transitions:
            if transition.current_state not in self.states:
                print(f"Invalid transition. {transition.current_state} is not a valid state.")
                return
            if transition.next_state not in self.states:
                print(f"Invalid transition. {transition.next_state} is not a valid state.")
                return
        self.transitions = transitions
        self.valid_transitions = True

    def __accept__(self, current_state, state_input):
        """Looks to see if the input for the given state matches a transition rule"""
        if state_input in self.inputs_allowed:
            for rule in self.transitions:
                if rule.match(current_state, state_input):
                    return rule.next_state
            print("No transition for state and input")
            return None
        return None

    def __return__(self, return_amount):
        self.current_state = self.__accept__(self.current_state, 1)
        # print(f"Ending state is {current_state}")

    def cash_in_and_return(self):
        cash = int(input("Please Enter the amount: "))
        self.current_state = self.__accept__(self.current_state, 1)
        Return = cash - self.COST[self.i - 1]
        # print(f"Current state is {current_state}")
        if self.current_state is None:
            return False
        self.__return__(Return)

    def refilling(self):
        print("All cans SOLD OUT. Needs REFILL")
        self.current_state = self.__accept__(self.current_state, 0)
        # print(f"Current state is {current_state}")
        print("User needs to type REFILL to replenish stock and continue transactions")

        while True:
            ref = input("Enter correct input: ")
            self.current_state = self.__accept__(self.current_state, ref)
            # print(f"Ending state is {current_state}")
            if self.current_state == 'idle':
                print("Refilling the Stocks of Vending Machine...")
                self.quantity[0] = self.no_of_cans * 8
                for j in range(1, 9):
                    self.quantity[j] = self.no_of_cans
                return self.current_state in self.accepting_states

    def vending_machine(self, code):

        # Check if we have transitions
        global cash, Return
        if not self.valid_transitions:
            print("Cannot process sequence without valid transitions")

        # print(f"Starting at {self.initial_state}")
        # we simply check if the initial state is an accepted one

        if code is None:
            return self.initial_state in self.accepting_states

        # Let's process the initial state
        self.current_state = self.__accept__(self.initial_state, code)
        # print(f"Current state is {current_state}")
        if self.current_state is None:
            return False
        self.drink = self.current_state

        for i in range(1, 9):
            if self.current_state is states[i]:
                self.i = i
                if self.quantity[i] == 0:
                    print(f"All cans of {self.current_state} are sold out. No cans available")
                    self.current_state = self.__accept__(self.current_state, 0)
                    # print(f"Current state is {current_state}")
                    if self.quantity[0] == 0:
                        return self.refilling()

                    else:
                        print("Choose other Drink which are available")
                        self.current_state = self.__accept__(self.current_state, 1)
                        # print(f"Current state is {current_state}")
                        return True

                elif self.quantity[i] > 0:
                    return self.cash_in_and_return()

                else:
                    print("Wrong Number of Cans in data")
                    return False
                # break

        if self.current_state is None:
            return False

        if self.current_state == 'Cash in and Return':

            if Return < 0:
                print("Insufficient balance\nTransaction Failure")
                print(f"Returning cash of {cash} bucks.")
                return False
            self.quantity[self.i] = self.quantity[self.i] - 1
            self.quantity[0] = self.quantity[0] - 1
            if Return > 0:
                print(f"Returning the change of {Return} bucks")
            print(f"Dispatching Drink can of {self.drink}")
            # print("See you soon")
            return True


"""this condition runs only the code inside the if statement"""
if __name__ == '__main__':

    no_of_cans = 0
    # total_cans = no_of_cans * 8

    # Setting up FSM
    # Set of states
    states = ['idle', 'Pepsi', 'Mountain Dew', 'Dr. Pepper', 'Coke', 'Gatorade', 'Diet Coke', 'Minute Maid',
              'Tropicana', 'check_all', 'Refill', 'Cash in and Return', 'Error']
    # Set of allowed inputs
    inputs_allowed = ['PEPS', 'MDEW', 'DPEP', 'COKE', 'GATO', 'DCOK', 'MINM', 'TROP', 0, 1, 'REFILL']

    # Set of Constant Cost of Cans
    COST = [30, 30, 50, 20, 20, 30, 25, 30]
    # Set of states that machine will accept its input on if it has fully consumed the input and has ended execution
    accepting_states = ['idle']
    # The initial state
    initial_state = 'idle'
    # Initializing each variety of juice
    # quantity = [total_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans, no_of_cans]
    fsm = FSM(states, inputs_allowed, accepting_states, initial_state, no_of_cans, COST)

    # Creating the set of all possible transitions
    prim_trans1 = Transition('idle', 'PEPS', 'Pepsi')
    prim_trans2 = Transition('idle', 'MDEW', 'Mountain Dew')
    prim_trans3 = Transition('idle', 'DPEP', 'Dr. Pepper')
    prim_trans4 = Transition('idle', 'COKE', 'Coke')
    prim_trans5 = Transition('idle', 'GATO', 'Gatorade')
    prim_trans6 = Transition('idle', 'DCOK', 'Diet Coke')
    prim_trans7 = Transition('idle', 'MINM', 'Minute Maid')
    prim_trans8 = Transition('idle', 'TROP', 'Tropicana')
    sec_trans1 = Transition('Pepsi', 0, 'check_all')
    sec_trans2 = Transition('Mountain Dew', 0, 'check_all')
    sec_trans3 = Transition('Dr. Pepper', 0, 'check_all')
    sec_trans4 = Transition('Coke', 0, 'check_all')
    sec_trans5 = Transition('Gatorade', 0, 'check_all')
    sec_trans6 = Transition('Diet Coke', 0, 'check_all')
    sec_trans7 = Transition('Minute Maid', 0, 'check_all')
    sec_trans8 = Transition('Tropicana', 0, 'check_all')
    sec_trans11 = Transition('Pepsi', 1, 'Cash in and Return')
    sec_trans12 = Transition('Mountain Dew', 1, 'Cash in and Return')
    sec_trans13 = Transition('Dr. Pepper', 1, 'Cash in and Return')
    sec_trans14 = Transition('Coke', 1, 'Cash in and Return')
    sec_trans15 = Transition('Gatorade', 1, 'Cash in and Return')
    sec_trans16 = Transition('Diet Coke', 1, 'Cash in and Return')
    sec_trans17 = Transition('Minute Maid', 1, 'Cash in and Return')
    sec_trans18 = Transition('Tropicana', 1, 'Cash in and Return')
    ter_trans1 = Transition('check_all', 1, 'idle')
    ter_trans2 = Transition('check_all', 0, 'Refill')
    ter_trans11 = Transition('Cash in and Return', 1, 'idle')
    quad_trans1 = Transition('Refill', 'REFILL', 'idle')

    transitions = [prim_trans1, prim_trans2, prim_trans3, prim_trans4, prim_trans5, prim_trans6, prim_trans7,
                   prim_trans8, sec_trans1, sec_trans2, sec_trans3, sec_trans4, sec_trans5, sec_trans6, sec_trans7,
                   sec_trans8, sec_trans11, sec_trans12, sec_trans13, sec_trans14, sec_trans15, sec_trans16,
                   sec_trans17, sec_trans18, ter_trans1, ter_trans2, ter_trans11, quad_trans1]

    # Verify and add them to the FSM
    fsm.add_transitions(transitions)

    # Vending Machine will continue to run in loop
    while True:
        print_list_of_juices()
        Code = input("Enter Code of Drink you want to purchase: ")
        # Execution of function starts
        Status = fsm.vending_machine(Code)
        print("ERROR!!!") if Status is False else print("Transaction Complete\nTHANK YOU")
