"""
Using the model obtained in the previous exercise, predict the women’s winning
time at the 2012 and 2016 Olympic games.
"""
from ex1_06 import *

def main():
    print(f"2012 winner has a time of {model(2012)}")
    print(f"2016 winner has a time of {model(2016)}")

if __name__ == "__main__":
    main()