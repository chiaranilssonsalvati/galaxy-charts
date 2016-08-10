import csv
import matplotlib.pyplot as plt
data_open = open("galaxies.csv", "rU")
data_in = list(csv.reader(data_open))

'''

greenlist =[]
redlist = []

for item in data_in[1:]:
	g_mag = item[0]
	r_mag = item[1]
	greenlist.append(g_mag)
	redlist.append(r_mag)

plt.xlabel("Green Value")
plt.ylabel("Red Value")


plt.hexbin(greenlist,redlist)
'''

r_g_list = []
for item in data_in[1:]:
	r_g = float(item[2])
	r_g_list.append(r_g)
allcolors = list(range(-1,1))
plt.xlabel("Color value")
plt.ylabel("Frequency")
plt.title("Frequency of different colors among galaxies")
plt.hist(r_g_list, range=[0, 2])


plt.show()
plt.close()
data_open.close()