
# Star
def create_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()


create_star_pattern(5)
