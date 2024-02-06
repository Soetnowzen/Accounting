import io


def execute_event(N, Q, input_string):
    buffer = io.StringIO(input_string)
    stateMachine = StateMachine(N)
    for _ in range(Q):
        line = buffer.readline().split()
        match line[0]:
            case "SET":
                i = int(line[1])
                x = int(line[2])
                if 1 <= i and i <= N and 1 <= x and x <= pow(10, 4):
                    stateMachine.set_command(i, x)
            case "PRINT":
                i = int(line[1])
                if 1 <= i <= N:
                    stateMachine.print_command(i)
            case "RESTART":
                x = int(line[1])
                if 0 <= x and x <= pow(10, 4):
                    stateMachine.restart_command(x)
            case _:
                print("Unkown command", line)

class StateMachine():
    def __init__(self, N) -> None:
        self.persons = [0]*N

    def set_command(self, i, x):
        """
        An event of type "SET i x" means that the ith person’s wealth is set to x
        """
        self.persons[i-1] = x

    def print_command(self, i):
        """
        An event of type “PRINT i” reports the current wealth of the ith person.
        """
        print(self.persons[i-1])

    def restart_command(self, x):
        """
        An event of type "RESTART x" means that the simulation is restarted, and everybody’s wealth is set to x.
        """
        for i in range(len(self.persons)):
            self.persons[i] = x
