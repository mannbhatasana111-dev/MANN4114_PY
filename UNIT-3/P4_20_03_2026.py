class OuterClass:

    def __init__(self):
        self.inner_obj = self.InnerClass()

    def outer_method(self):
        print("OUTER class")

    class InnerClass:
        def inner_method(self):
            print("INNER class")

obj = OuterClass()

obj.outer_method()
obj.inner_obj.inner_method()