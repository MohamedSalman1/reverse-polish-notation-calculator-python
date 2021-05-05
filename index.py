import sys
import re


class RpnCalculator:

    def __init__(self):
        self.all_numbers = []
        self.all_operators = []
        self.allowed_operators = ['+', '-', '*', '/']
        self.exit_statements = ['q', 'quit', 'exit']
        self.invalid_calculation = (
            "Numbers not available to process calculation, " +
            "try inputting a number first"
        )
        self.empty_input = "Please enter a number or an operator(+ - * /)"

    def calculate(self, user_input):
        all_numbers_count = len(self.all_numbers)
        if len(self.all_operators) > 0:
            for idx, operator in enumerate(self.all_operators):
                try:
                    last = float(self.all_numbers[-1])
                except IndexError:
                    continue

                try:
                    second_last = float(self.all_numbers[-2])
                except IndexError:
                    continue

                if operator == '+':
                    value = second_last + last
                if operator == '-':
                    value = second_last - last
                if operator == '*':
                    value = second_last * last
                if operator == '/':
                    value = second_last / last

                self.all_numbers.pop()
                self.all_numbers.pop()
                self.all_numbers.append(str(value))

            self.all_operators = []

        if all_numbers_count <= 1 and user_input in self.allowed_operators:
            print(self.invalid_calculation)
            self.get_input()
            return
        return self.all_numbers[-1]

    def get_input(self):
        user_input = input("> ")
        if user_input == '' or user_input is None:
            print(self.empty_input)
            self.get_input()
            return
        if (user_input in self.exit_statements):
            sys.exit()

        parsed_input = user_input.split(sep=" ")
        parsed_input = list(filter(None, parsed_input))

        for element in parsed_input:
            if element in self.allowed_operators:
                self.all_operators.append(element)
                continue
            if re.match(r'^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$', element):
                self.all_numbers.append(element)

        output = self.calculate(user_input)
        print(output)

        self.get_input()
        return


objRpn = RpnCalculator()
objRpn.get_input()
