import matplotlib.pyplot as plt
import csv

sim_time = []
sim_v = []
size = 0
with open('results.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i = 0.0
    for row in plots:
        sim_time.append(float(i))
        sim_v.append(float(row[3]))
        i += float(row[0])
        size += 1

log_v = []
log_time = []
with open('endu_merge.log', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    i = 0
    for row in plots:
        log_v.append(float(row[1]))
        i += 1
        if i == size:
            break


plt.plot(sim_time, log_v, color='r', linewidth=.5)
plt.plot(sim_time, sim_v, color='y', linewidth=.5)
plt.grid()
plt.legend()
plt.show()
