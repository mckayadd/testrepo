# src/my_math/__main__.py
from . import add, mul

def main():
    print("my_math demo")
    print("2 + 3 =", add(2, 3))
    print("4 * 5 =", mul(4, 5))

if __name__ == "__main__":
    main()
