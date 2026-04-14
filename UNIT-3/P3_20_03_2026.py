class Trip:
    main_name = 'Mann, Hemang, Yuvraj, Pragnesh'
    
    def __init__(self, name):
        self.n = name
        
    def going(self):
        print("On Trip Main Person : ", self.n)
        
    @classmethod
    def main_going(cls):
        print("On Trip Main Persons : ", cls.main_name)



trip1 = Trip("Het")

Trip.main_going()
trip1.going()
