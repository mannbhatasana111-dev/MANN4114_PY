class Temperature:

    def convertFarenheit(self, c):
        print((c * 9 / 5) + 32)

    def convertCelsius(self, f):
        print((f - 32) * 5 / 9)


t = Temperature()
user_c = float(input("Enter temperature in Celsius: "))
t.convertFarenheit(user_c)

user_f = float(input("Enter temperature in Fahrenheit: "))
t.convertCelsius(user_f)