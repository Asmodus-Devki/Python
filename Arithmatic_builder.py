def arithmetic_arranger(problems, show_answers=False):
    # Error handling
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = []
    bottom_row = []
    dashes = []
    solutions = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        # Check for valid operator
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Check if numbers are digits and within the limit
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width for formatting
        width = max(len(num1), len(num2)) + 2
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)
        solutions.append(str(eval(problem)).rjust(width))

    # Join the rows with four spaces
    arranged_problems = '    '.join(top_row) + '\n' + \
                        '    '.join(bottom_row) + '\n' + \
                        '    '.join(dashes)

    # Add solutions if required
    if show_answers:
        arranged_problems += '\n' + '    '.join(solutions)

    return arranged_problems

# Example usage

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))