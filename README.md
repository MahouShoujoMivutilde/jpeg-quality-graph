### Скрипт построения графиков размера и SSIM/PSNR в зависимости от % качества jpeg
---
#### Требования
* `python 3.4+ `
* * `matplotlib`
* * `pillow`
* * `psutil` (опционально, нужен для понижения приоритета дочерним процессам при обработке)
* `ffmpeg 3.x` в `PATH`

#### Использование
```
usage: jpeg_graph.py [-h] [-s] [-p] -i I

Строит график зависимости объективного качества (PSNR/SSIM) и размера файла от
% качества jpeg, требует matplotlib, Pillow и опционально psutil, а также
ffmpeg 3.x в PATH

optional arguments:
  -h, --help  show this help message and exit
  -s          Не удалять папку с полученными jpeg
  -p          Подписать соответствующие розовым линиям отметки на OY

required named arguments:
  -i I        Путь к исходному изображению / к папке с исходными изображениями
              (для расчета усредненного графика)
```

#### Примеры результатов

##### PNG изображения в аниме-стиле

![](https://i.imgur.com/Ra7mAk0.png)

![](https://i.imgur.com/Tua6jCb.png)

![](https://i.imgur.com/6CP0f4q.png)

---

##### JPEG фото с качеством 100%, отрендеренные из raw

![](https://i.imgur.com/nIHYHf0.png)

![](https://i.imgur.com/la6bSf1.png)

![](https://i.imgur.com/h8hwiGx.png)

---

##### TIFF фото, сжатие без потерь, отрендеренные из raw

![](https://i.imgur.com/SFWbNUZ.png)

![](https://i.imgur.com/nOUxtQH.png)

![](https://i.imgur.com/EIRTnDQ.png)

---
__ps__ выборка везде 100 изображений.