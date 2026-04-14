import matplotlib.pyplot as plt

years = ['2021', '2022', '2023', '2024', '2025']
profit = [50000, 65000, 80000, 75000, 95000]

plt.plot(years, profit, marker='o', color='green', linestyle='--')
plt.title('5 Year Profit Analysis')
plt.xlabel('Year')
plt.ylabel('Profit (USD)')
plt.grid(True)
plt.show()