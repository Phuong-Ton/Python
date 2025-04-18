def print_2_line():
    print("*****")
    print("*****")
    
def print_1_star():
    print("  *")

def print_2_star():
    print(" * *")
    
def print_5_star():
    print_2_star()
    print_1_star()
    print_2_star()


def print_1st_part():
    print_2_line()
    print_5_star()
    print()
    
def print_2nd_part():
    print_2_line()
    print_5_star()
    print_2_line()
    print()

def print_3rd_part():
    print_1_star()
    print_1_star()
    print_1_star()
    print_2_line()
    print_5_star()

def main():
    print_1st_part()
    print_2nd_part()
    print_3rd_part()

main()
