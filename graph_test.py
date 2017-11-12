from random import randint, random
from os import remove, listdir
import re
import jpeg_graph

if __name__ == '__main__':
    for t in listdir():
        if re.match('graph_test\d\, min_y.+', t):
            try:
                remove(t)
                print('-{}'.format(t))
            except Exception as e:
                print(e)
    print('\n\n')
    for i in range(10):
        t = randint(5, 50)
        
        ox = [i for i in range(1, t + 1)]
        oy = sorted([random() for i in range(1, t + 1)])
        print('+график {}, минимальный y: {}'.format(i, min(oy)))
        jpeg_graph.draw2(ox, oy, '', 'graph_test{}, min_y {}'.format(i, min(oy)), 'какое-то значение объективного качества', False, 'какое-то значение качества формата')