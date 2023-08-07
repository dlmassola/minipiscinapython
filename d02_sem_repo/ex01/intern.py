class Intern:

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
        
    def __init__(self, name = 'My name? I\'m nobody, an intern, I have no name.'):
        self.name = name
        
    def __str__(self):
        return self.name

    def work(self):
        raise Exception('I\'m just an intern, I can\'t do that...')
    
    def make_coffee(self):
        return Intern.Coffee()
    

if __name__ == '__main__':
    
    class1 = Intern()
    print(class1)

    class2 = Intern("Mark")
    print(class2)
    print(class2.make_coffee())

    try:
        class1.work()
    except Exception as e:
        print("Description error:", str(e))