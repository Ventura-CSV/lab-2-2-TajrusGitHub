def main():
    workhours = int(input('Enter your work hours: 28'))  # Removed the hardcoded value
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

    # Calculate overtime and regular wage
    if workhours > reg_hours:
        overtime = workhours - reg_hours
        overtime_wage = overtime * ov_rate
        regular_wage = reg_hours * reg_rate
    else:
        overtime = 0
        overtime_wage = 0
        regular_wage = workhours * reg_rate

    # Calculate total wage
    total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage:.2f}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

    return regular_wage, overtime_wage, total_wage

if __name__ == '__main__':
    main()

