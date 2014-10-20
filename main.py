from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import os
import glob


font = {'family' : 'times new roman',
        'size' : 10}

plt.rc('font', **font)
plt.rcParams['legend.fontsize'] = 10

def main(x, ys):
    print x.__len__()
    fig = plt.figure(figsize = (6.7, 5))
    plt.grid(color='gray', linewidth=0.5, linestyle=':')

    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.set_xlabel(r'Rozegranych gier ($\times$1000)')
    ax1.set_ylabel(r'Odsetek wygranych gier $ [ \% ] $')

    ax2.set_xticklabels([0, 40, 80, 120, 160, 200])
    ax2.set_xlabel(r'Pokolenie')

    for n, y in ys.items():
        print n
        ax1.plot(x, y, label = n.split('.')[0])

    legend = ax1.legend(loc='lower right', fancybox = True, framealpha = 0.8)
    plt.savefig('E:\OneDrive\Studia\V semestr\KCK\Projekt1\myplot.png', dpi=210)
    plt.show()


def box(ys):

    data = []
    for i,y in ys.items():
        data.append(y)
    f = plt.figure(figsize = (3, 5))
    ax = f.add_subplot(111)
    ax.yaxis.tick_right()
    ax.set_xticklabels(range(5), rotation=20)
    plt.grid(color='gray', linewidth=0.5, linestyle=':')
    plt.boxplot(data,1, labels=[n.split('.')[0] for n, y in ys.items()], showmeans=True, meanprops=dict(marker=(0,3,0), markerfacecolor='blue', fillstyle='right', alpha=1.0))
    plt.savefig('boxplot.png', dpi=210)
    # plt.show()

if __name__ == '__main__':
    ys = {}
    x = []
    z = []
    for filename in sorted(glob.glob('*.csv')):
        with open(filename) as f:
            f.readline()
            x = []
            y = []
            z = []
            for line in f:
                # z.append(int(line.split(',')[0]))
                x.append(int(line.split(',')[1])/1000)
                t = [float(i) for i in line.split(',')[2:]]
                y.append(sum(t)/t.__len__()*100)
                # y=map(lambda x: float(x), line.split(',')[2:])
            print y
        # ys.append(y)
        ys[filename] = y
    # main(x,ys)
    box(ys)