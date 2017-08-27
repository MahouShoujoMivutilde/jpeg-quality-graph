from PIL import Image
from multiprocessing import Pool
from functools import partial
from os import listdir, path, makedirs
import matplotlib.pyplot as plt
from shutil import rmtree
import argparse 
import subprocess 
import re

def get_args():
    parser = argparse.ArgumentParser(description = "Строит график зависимости SSIM от % качества jpeg, требудет matplotlib и Pillow, а также ffmpeg 3.x в PATH")
    parser.add_argument("-s", default = False, action = "store_true", help = "Не удалять папку с полученными jpeg")
    parser.add_argument("-p", default = False, action = "store_true", help = "Подписать соответствующие розовым линиям отметки на OY")
    requiredNamed = parser.add_argument_group("required named arguments")
    requiredNamed.add_argument("-i", required = True, help = "Путь к исходному изображению")
    return parser.parse_args()

def to_jpeg(q, base, dst):
    base.convert('RGB').save(r'{}\{}.jpeg'.format(dst, q), quality = q)

def get_jpegs(folder):
    return [path.join(folder, i) for i in listdir(folder) if '.jpeg' in i]

# https://github.com/MahouShoujoMivutilde/ffmpeg_ssim
def get_ssim(ref_img, cmp_img):
    p = subprocess.Popen(['ffmpeg.exe', '-loglevel', 'error', '-i', ref_img, '-i', cmp_img, '-filter_complex', 'ssim=stats_file=-', '-f', 'null', '-'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    p.wait()
    outs, _ = p.communicate()
    return float(re.search(r'\bAll:(\d+(?:\.\d+)?)\s', outs.decode('utf-8')).group(0)[4:])

def meh(a, b):
    s = get_ssim(b, a)
    return s

def filter(ox, oy):
    fuchsia = []
    k = []
    for x, y in zip(ox, oy):
        if x % 5 == 0:
            fuchsia.append((x, y))
        else:
            k.append((x, y))
    return(fuchsia, k)

def extract_x(lst):
    return list(zip(*lst))[0]

def extract_y(lst):
    return list(zip(*lst))[1]

def draw2(ox, oy, name, tp, new_alg):
    min_size = min(oy)
    plt.subplots(figsize = (10, 10))
    plt.plot(ox, oy, 'ro', markersize = 2)
    f, k = filter(ox, oy)
    plt.vlines(extract_x(k), [0], extract_y(k), lw = 0.5)
    plt.vlines(extract_x(f), [0], extract_y(f), lw = 0.5, color = 'fuchsia')
    plt.xticks(range(0, 101, 5))
    plt.yticks(extract_y(f) if new_alg else [round(min_size + i*(max(oy) - min_size)/24, 4) for i in range(0, 24)] + [max(oy)])
    plt.axis([1, 100, min_size, max(oy)])
    plt.xlabel('jpeg качество, %')
    plt.ylabel(tp)
    plt.tight_layout()
    plt.savefig('{}_{}_graph.png'.format(name, tp), dpi = 200)


def process(base_path, new_alg, store = False):
    folder = path.splitext(base_path)[0]
    makedirs(folder)
    print('генерируем jpeg...')
    with Image.open(base_path) as base:
        with Pool() as pool:
            pool.map(partial(to_jpeg, base = base, dst = folder), [q for q in range(1, 101)])   
    jpegs = get_jpegs(folder)
    print('рассчитываем SSIM...')
    with Pool() as pool:
        ssims = pool.map(partial(meh, b = base_path), jpegs)
    ox = [int(path.split(i)[1].split('.')[0]) for i in jpegs]
    print('рисуем графики...')
    draw2(ox, ssims, folder, 'SSIM', new_alg)
    draw2(ox, [path.getsize(i)/1024 for i in jpegs], folder, 'размер, kb', new_alg)
    if not store:
        rmtree(folder)

if __name__ == '__main__':
    args = vars(get_args())
    process(args['i'], args['p'], store = args['s'])