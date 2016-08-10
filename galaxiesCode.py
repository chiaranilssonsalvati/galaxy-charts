import csv
import matplotlib.pyplot as plt
import numpy as np
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


cm = plt.cm.get_cmap('RdYlBu_r')
Y,X = np.histogram(r_g_list, 25, normed=1)
x_span = X.max()-X.min()
C = [cm(((x-X.min())/x_span)) for x in X]

plt.xlabel("Color value")
plt.ylabel("Frequency")
plt.title("Frequency of different colors among galaxies")
plt.bar(X[:-1],Y,color=C)

#width=X[1]-X[0])



#plt.hist(r_g_list, )


plt.show()
plt.close()
data_open.close()