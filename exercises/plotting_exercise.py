import matplotlib.pyplot as plt
import pandas as pd

# x = [1, 2, 3, 4, 5]
# y1 = [2, 3, 5, 7, 11]
# y2 = [1, 4, 6, 8, 10]

# plt.plot(x, y1, label="Linje 1", color="blue", linestyle="--")
# plt.plot(x, y2, label="Linje 2", color="red", linestyle=":")


# plt.title("Flera linjer i samma graf")
# plt.xlabel("X-axel")
# plt.ylabel("Y-axel")

# plt.show()

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# plt.scatter(x,y,color = "green")

# plt.title("Scatter Plot")
# plt.xlabel("X-axel")
# plt.ylabel("Y-axel")

# plt.show()

# plt.savefig("plot_image.png")

# x = ["A","B","C","D","E"]
# y = [10, 15, 7 ,20 ,12]

# plt.bar(x,y)

# plt.title("Stapel-diagram")
# plt.xlabel("X Axel")
# plt.ylabel("Y Axel")

# plt.show()

df = pd.read_csv("data/coffee.csv")

print(df)

day_order = ['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']

df['Day'] = pd.Categorical(df['Day'],categories=day_order,ordered= True)

pivot_df = df.pivot_table(index='Day', columns="Coffee Type", values="Units Sold",aggfunc= "sum",observed= False)

pivot_df.plot(kind="bar",figsize=(10,6),color=['black','blue'])

plt.title("Coffee Sales per Day")
plt.xlabel("Day of week")
plt.ylabel("Units Sold")

plt.tight_layout()
plt.show()





