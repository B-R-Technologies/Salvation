class User:
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
        
        user = User("Brian", "Wanjala")
        print(User.first)
        print(User.last)
    