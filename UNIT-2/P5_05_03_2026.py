try:
    filename = "test.text"

    with open(filename, "r") as f:
        content = f.read()

        print("--- File Content ---")
        print(content)
        print("--------------------")
        words = content.split()
        word_count = len(words)
        print(f"Total number of words in file: {word_count}")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")