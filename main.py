from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import os
import glob


font = {'family' : 'times new roman',
        'size' : 10}

plt.rc('font', **font)
plt.rcParams['legend.fontsize'] = 10

def markGen():
    markers = ['o-', '^-', 'D-', 'd-', 's-']
    while True:
        for m in markers:
            yield m

def main(x, ys, ys2):
    print x.__len__()
    fig = plt.figure(figsize = (6.7, 5))


    ax = fig.add_subplot(111)
    ax1 = fig.add_subplot(121)
    ax2 = ax1.twiny()

    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

    ax1.grid(color='gray', linewidth=0.5, linestyle=':')

    ax1.set_xlabel(r'Rozegranych gier ($\times$1000)')
    ax1.set_ylabel(r'Odsetek wygranych gier $ [ \% ] $')

    ax2.set_xticklabels([0, 40, 80, 120, 160, 200])
    ax2.set_xlabel(r'Pokolenie')

    marker = markGen()

    for n, y in ys.items():
        print n
        ax1.plot(x, y, marker.next(), markevery=25, label = n.split('.')[0])

    legend = ax1.legend(loc='lower right', fancybox = True, framealpha = 0.8)

    data = []
    for i,y in ys2.items():
        data.append(y)
    f = fig.add_subplot(122)
    f.yaxis.tick_right()
    f.axis([0, len(ys2), 60, 100])
    l = [n.split('.')[0] for n, y in ys.items()]
    plt.boxplot(data,1, showmeans=True, meanprops=dict(marker=(0,3,0), markerfacecolor='blue', fillstyle='right', alpha=1.0))
    f.set_xticks(range(1,len(ys2)+1))
    f.set_xticklabels(l, rotation=20)
    f.grid(color='gray', linewidth=0.5, linestyle=':')



    plt.savefig('E:\OneDrive\Studia\V semestr\KCK\Projekt1\myplot.pdf', dpi=130)
    # plt.show()


def box(ys):

    data = []
    for i,y in ys.items():
        data.append(y)
    f = plt.figure(figsize = (3, 5))
    ay = f.add_subplot(111)
    ay.yaxis.tick_right()
    ay.set_xticklabels(range(5), rotation=20)
    plt.grid(color='gray', linewidth=0.5, linestyle=':')
    plt.boxplot(data,1, labels=[n.split('.')[0] for n, y in ys.items()], showmeans=True, meanprops=dict(marker=(0,3,0), markerfacecolor='blue', fillstyle='right', alpha=1.0))
    # plt.savefig('boxplot.png', dpi=210)
    # plt.show()

if __name__ == '__main__':
    ys = {}
    x = []
    ys2 = {}
    for filename in sorted(glob.glob('*.csv')):
        with open(filename) as f:
            f.readline()
            x = []
            y = []
            for line in f:
                # z.append(int(line.split(',')[0]))
                x.append(int(line.split(',')[1])/1000)
                t = [float(i)*100 for i in line.split(',')[2:]]
                y.append(sum(t)/t.__len__())
                # y=map(lambda x: float(x), line.split(',')[2:])
            print y
        # ys.append(y)
        ys2[filename] = t
        ys[filename] = y
    main(x,ys, ys2)
    # box(ys2)