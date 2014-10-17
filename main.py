from __future__ import division

import matplotlib.pyplot as plt
import os
import glob

font = {'family' : 'times new roman',
        'size' : 10}

plt.rc('font', **font)
plt.rcParams['legend.fontsize'] = 10

def main(x, ys):
    print x.__len__()
    plt.figure(figsize = (6.7, 5))
    plt.grid(color='gray', linewidth=0.5, linestyle=':')
    plt.xlabel('Rozegranych gier (x1000)')
    plt.ylabel('Odsetek wygranych gier [%]')
    for n, y in ys.items():
        print n
        plt.plot(x, y, label = n.split('.')[0])

    legend = plt.legend(loc='lower right', fancybox = True, framealpha = 0.8)
    plt.savefig('E:\OneDrive\Studia\V semestr\KCK\Projekt1\myplot.png', dpi=210)
    plt.close()


if __name__ == '__main__':
    ys = {}
    x = []
    for filename in sorted(glob.glob('*.csv')):
        with open(filename) as f:
            f.readline()
            x = []
            y = []
            for line in f:
                z = int(line.split(',')[0])
                x.append(int(line.split(',')[1])/1000)
                t = [float(i) for i in line.split(',')[2:]]
                y.append(sum(t)/t.__len__()*100)
                # y=map(lambda x: float(x), line.split(',')[2:])
            print y
        # ys.append(y)
        ys[filename] = y
    main(x,ys)