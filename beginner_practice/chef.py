class Chef:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def cook(self):
        print(f"{self.name} is cooking.")

    def prepare_ingredients(self):
        print(f"{self.name} is preparing ingredients.")

    def clean_kitchen(self):
        print(f"{self.name} is cleaning the kitchen.")