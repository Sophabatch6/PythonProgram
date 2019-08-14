import sys


class IOContainer:
    message = ""

    def read_input(self):
        self.message = input(">>>>>")

    def print_message(self):
        if self.message is "":
            print("Nothing to display.")
        else:
            print(self.message)

    def reset_message(self):
        self.message = ""
        obj.read_input()


obj = IOContainer()

obj.read_input()
obj.print_message()
obj.reset_message()
obj.print_message()
