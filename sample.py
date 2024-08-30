import importlib as il
import test

il.reload(test)

def main():
    print(test.x)
    test.foo()

main()