### Скрипт построения графиков размера и SSIM/PSNR в зависимости от % качества jpeg
---
#### Требования
* `python 3.4+ `
* * `matplotlib`
* * `pillow`
* `ffmpeg 3.x` в `PATH`

#### Использование
```
usage: jpeg_graph.py [-h] [-s] [-p] -i I

Строит график зависимости объективного качества (PSNR/SSIM) и размера файла от
% качества jpeg, требудет matplotlib и Pillow, а также ffmpeg 3.x в PATH

optional arguments:
  -h, --help  show this help message and exit
  -s          Не удалять папку с полученными jpeg
  -p          Подписать соответствующие розовым линиям отметки на OY

required named arguments:
  -i I        Путь к исходному изображению
```

#### Пример результата
![](https://i.imgur.com/SRgyHox.png)
![](https://i.imgur.com/AD6Mp89.png)
![](https://i.imgur.com/juVizaR.png)
