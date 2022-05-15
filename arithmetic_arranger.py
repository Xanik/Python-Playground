import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def arithmetic_arranger(problems, solver=False):
    # Check problems does not exceed the given max(5)
    if len(problems) > 5:
        return "Error: Too many problems."
    toptier = ""
    bottomtier = ""
    lines = ""
    totals = ""
    for n in problems:
        fnumber = n.split()[0]
        operator = n.split()[1]
        snumber = n.split()[2]

        # Handle errors for input:
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not fnumber.isdigit() or not snumber.isdigit():
            return "Error: Numbers must only contain digits."
        if len(fnumber) > 4 or len(snumber) > 4:
            return "Error: Numbers cannot be more than four digits"

        # Get total of correct function
        total = ops[operator](int(fnumber), int(snumber))
        # Get distance for longest operator
        operatorDistance = max(len(fnumber), len(snumber)) + 2

        snumber = operator + snumber.rjust(operatorDistance - 1)
        toptier = toptier + fnumber.rjust(operatorDistance) + (4 * " ")
        bottomtier = bottomtier + snumber + (4 * " ")
        lines = lines + len(snumber) * "_" + (4 * " ")
        totals = totals + str(total).rjust(operatorDistance) + (4 * " ")
    if solver:
        print(toptier)
        print(bottomtier)
        print(lines)
        print(totals)


if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
