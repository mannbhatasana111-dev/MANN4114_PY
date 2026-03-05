import logging
logging.basicConfig(filename='demo.log', level=logging.ERROR)

try:
    result = 10 / 0

except ZeroDivisionError as e:
    logging.error(f"Arithmetic Error occurred: {e}")
    print("Error captured! Check demo.log in this folder.")