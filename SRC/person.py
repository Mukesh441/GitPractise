class person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def display_info(self):
        print(f"My name is {self.first_name} {self.last_name}")
        