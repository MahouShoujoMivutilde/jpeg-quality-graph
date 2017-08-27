
#### Требования
* `python 3.4+ `
* * `matplotlib`
* * `pillow`
* `ffmpeg 3.x` в `PATH`

#### Использование
```
usage: jpeg_ssim_graph.py [-h] [-s] [-p] -i I

Строит график зависимости SSIM от % качества jpeg, требудет matplotlib и
Pillow, а также ffmpeg 3.x в PATH

optional arguments:
  -h, --help  show this help message and exit
  -s          Не удалять папку с полученными jpeg
  -p          Подписать соответствующие розовым линиям отметки на OY

required named arguments:
  -i I        Путь к исходному изображению
```

#### Пример результата
![](https://i.imgur.com/JcJWvSF.png)
![](https://i.imgur.com/uMBll66.png)