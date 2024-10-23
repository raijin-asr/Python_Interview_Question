"""
Does Python have a main() Function?
No, Python does not have a main() function. However, we can simulate it using the __name__ attribute of a module.

In Python, if the module is run independently, the value of the inbuilt attribute __name__ is always '__main__'.

So, we can create an if condition to check if the file is executed from the module itself. And if it is, run the main() function by creating it manually. Here's an example,"""

def main():
    print('this is main function')
 
if __name__ == '__main__':
    main()