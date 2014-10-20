from matplotlib import pyplot as plt
import matplotlib as mpl
import glob
import matplotlib.lines as mlines


for filename in sorted(glob.glob('*.csv')):
    with open(filename) as f:
        f.readline()
        x = []
        for line in f:
            t = [float(i) for i in line.split(',')[2:]]
            x.append(sum(t)/len(t))
        print '{0}: {1}'.format(filename, sum(x)/len(x))

        x.sort()

        xlen = len(x)
        print('mediana: {0}'.format(x[len(x)/2]))
        print('pierwszy kwartyl: {0}'.format(x[int(xlen*0.25)]))
        print('trzeci kwartyl: {0}'.format(x[int(xlen*0.75)]))
