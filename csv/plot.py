import matplotlib.pyplot as plt
import csv
import copy

# Plot voltage
y = []
with open('data.csv', 'r') as csvfile:
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
#d = []
#with open('data.csv', 'r') as csvfile:
#    plots = csv.reader(csvfile, delimiter=',')
#    for row in plots:
#        d.append(float(row[4]))
#
#e = []
#f = []
#with open('results.csv', 'r') as csvfile:
#    plots = csv.reader(csvfile, delimiter=',')
#    i = 0.0
#    for row in plots:
#        e.append(float(i))
#        f.append(float(row[2]))
#        i += float(row[0])
#
#plt.plot(e, d, color='r')
#plt.plot(e, f, color='y')

# Plot SOC
y = []
with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(float(row[1]))

x = []
z = []
with open('results.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i = 0.0
    for row in plots:
        x.append(float(i))
        z.append(float(row[1]))
        i += float(row[0])


plt.plot(x, y, color='r')
plt.plot(x, z, color='y')

plt.legend()
plt.show()
