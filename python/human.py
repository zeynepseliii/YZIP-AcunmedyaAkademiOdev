class Human:
    name = "Halit"
    #built-in
    #constructor
    #initalize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence): 
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")
    