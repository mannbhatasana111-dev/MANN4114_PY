class A:
    def show(self):
        print("This is class A")

class B:
    def show(self):
        print("This is class B")

class C(A, B):
    pass

obj = C()

obj.show()

print("\nMethod Resolution Order (MRO):")
for i in C.mro():
    print(i)