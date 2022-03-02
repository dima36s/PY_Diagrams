import random
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (11,5)
#
data_x = list(range(1950, 2022, 5))
len_x = len(data_x)
data_vvp = list(random.randrange(100, 500) for i in range(len_x))
data_vvp2 = list(random.randrange(100, 500) + i * 100 for i in range(len_x))
data_vvp3 = list(random.randrange(100, 500)+1000-i * 100 for i in range(len_x))
# print(*data_x)
# print(*data_vvp)
# print(*data_vvp2)
print(*data_vvp3)

plt.plot(data_x, data_vvp3, color='red', marker='.')
plt.plot(data_x, data_vvp2, color='blue', marker='.')
plt.title('VVP for some country')
plt.ylabel('Milliards $')
plt.show()
# FILMS

data_stars = list(random.randrange(1, 10) for i in range(len_x))
print(*data_stars)

data_films = list(f"film {i}" for i in range(len_x))
print(*data_films)

plt.bar(range(len(data_films)), data_stars)
plt.title('MY Beast Films')
plt.ylabel('Number of stars')
plt.xticks(range(len(data_films)), data_films)
plt.show()
