import io


class StateMachine:
    def __init__(self, num_persons):
        """Initialize the StateMachine with a given number of persons."""
        self.persons = [0] * num_persons

    def set_command(self, i, x):
        """An event of type "SET i x" means that the ith person’s wealth is set to x"""
        self.persons[i - 1] = x

    def print_command(self, i):
        """An event of type “PRINT i” reports the current wealth of the ith person."""
        print(self.persons[i - 1])

    def restart_command(self, x):
        """An event of type "RESTART x" means that the simulation is restarted, and everybody’s wealth is set to x."""
        for i in range(len(self.persons)):
            self.persons[i] = x

def execute_event(num_persons, num_queries, input_data):
    """Execute a series of events on a StateMachine."""
    buffer = io.StringIO(input_data)
    state_machine = StateMachine(num_persons)

    for _ in range(num_queries):
        line = buffer.readline().split()

        try:
            command, *args = line
            args = list(map(int, args))

            if command == "SET":
                i, x = args
                if 1 <= i <= num_persons and 1 <= x <= 10_000:
                    state_machine.set_command(i, x)
            elif command == "PRINT":
                i, = args
                if 1 <= i <= num_persons:
                    state_machine.print_command(i)
            elif command == "RESTART":
                x, = args
                if 0 <= x <= 10_000:
                    state_machine.restart_command(x)
            else:
                print("Unknown command:", line)

        except ValueError as e:
            print(f"Error processing command {line}: {e}")

# Example usage:
execute_event(5, 3, "SET 1 100\nPRINT 1\nRESTART 50")
