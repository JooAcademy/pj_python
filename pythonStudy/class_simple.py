class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    greeter = Greeter("World")
    print(greeter.greet())
    
    
    
    
class HelloWorld:
    def __init__(self):
        print("Hello, World!")

if __name__ == "__main__":
    hw = HelloWorld()
    
    
    
        
    
class HelloWorld:
    def __init__(self, greet):
        print(f"{greet}, World!")

if __name__ == "__main__":
    hw1 = HelloWorld("HI")
    hw2 = HelloWorld("Hello")
    hw3 = HelloWorld("My")
    hw4 = HelloWorld("Python")    