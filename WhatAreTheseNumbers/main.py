# Jackson Hauley - What are these numbers

# Defining Functions
def insert_commas(num):
    num = f"{num:,}"
    return num

def add_decimals(decimals,num):
    num = f"{num:.{decimals}f}"
    return num

def make_percentage(decimals,num):
    num = f"{num:.{decimals}%}"
    return num

def make_dollar():