vital = "Normal"

def show():
    print("Patient Vital:", vital)

def update():
    global vital
    vital = "Critical"

show()
update()
show()

'''
Global variables allow all functions to access the same patient data easily.
But they can make the program difficult to maintain and debug.
They may also cause security risks because sensitive data is accessible everywhere.
'''
