import matplotlib.pyplot as plt
import csv
import copy

data_file = 'data_ts.csv'
# Plot voltage
y = []
with open(data_file, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(float(row[3]))

x = []
z = []
with open('results.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i = 0.0
    for row in plots:
        x.append(float(i))
        z.append(float(row[3]))
        i += float(row[0])


# Plot current
y = []
with open(data_file, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(float(row[4]))

x = []
z = []
with open('results.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i = 0.0
    for row in plots:
        x.append(float(i))
        z.append(float(row[2]))
        i += float(row[0])

# Plot SOC
# y = []
# with open(data_file, 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         y.append(float(row[1]))
# 
# x = []
# z = []
# with open('results.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     i = 0.0
#     for row in plots:
#         x.append(float(i))
#         z.append(float(row[1]))
#         i += float(row[0])

plt.plot(x, y, color='r', linewidth=1)
plt.plot(x, z, color='y', linewidth=.5)
plt.grid()
plt.legend()
plt.show()
