from __future__ import division

import matplotlib.pyplot as plt

import glob


def main(x, ys):
    print x.__len__()
    plt.figure(figsize = (3, 3))
    for y in ys:
        plt.plot(x,y)
    plt.savefig('E:\OneDrive\Studia\V semestr\KCK\Projekt1\myplot.png', dpi=110)
    plt.close()


if __name__ == '__main__':
    print 'ok'

    ys=[]
    for filename in glob.glob('*.csv'):
        with open(filename) as f:
            f.readline()
            x=[]
            y=[]
            for line in f:
                z = int(line.split(',')[0])
                x.append(int(line.split(',')[1]))
                t=[float(i) for i in line.split(',')[2:]]
                y.append(sum(t)/t.__len__())
                # y=map(lambda x: float(x), line.split(',')[2:])
            print y
        ys.append(y)
    main(x,ys)

    tab = "34, 65, 23"

    print tab

    n = [int(x) for x in tab.split(', ')[1:]]

    print n