try:
    with open("test.text", "r") as s:
        data = s.read()
    with open("copytest.text", "w") as d:
        d.write(data)
    print("File copied successfully!")

except FileNotFoundError:
    print("Error: The source file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")