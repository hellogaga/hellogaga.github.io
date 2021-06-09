---
title: "Notebook"
last_modified_at: 2021-05-29T18:20:00+01:00

categories:
  - Notebook
tags:
  - programming
  - notebook
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

## Python
### Callback functions
TBC

### Parameters in functions
TBC


## Pandas
### Round timestamp
```python
# round the timestamp to min
df_plc['Time'] = df_plc['Time'].apply(lambda x: x.round('min'))
```

### Timestamp resampling
Reference page is [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.resample.html).

```python
# upsample a time series dataset. It is like group. 
akeb_data = akeb_data.set_index('Time')
akeb_data_resample = akeb_data.resample('5T').ffill()
```

## matplotlib
### Add Chinese fonts in Matplotlib figures. 
When I use matplotlib to generate pictures in Ubuntu, it sometimes cannot display Chinese characters. The solution is the method in this [page](https://programming.vip/docs/how-to-make-matplotlib-display-chinese-smoothly-in-ubuntu-16.04.html). A short summary is below: 
* use the following commands to check the fonts folder.
  ```python
  import matplotlib
  matplotlib.matplotlib_fname()
  ```
  In my environment, it gives the following location ```/home/yang/Desktop/weight&food/weight/lib/python3.9/site-packages/matplotlib/mpl-data/matplotlibrc```. This is a configuration file located in my local python virtual environment. 
* navigate to the folder ```/home/yang/Desktop/weight&food/weight/lib/python3.9/   site-packages/matplotlib/mpl-data/fonts/ttf/``` and paste a new chinese font file `simhei.ttf` to the folder. The font file can be found [here](/assets/others/simhei.ttf).
* edit the `matplotlibrc` file.  
  * The line `#font.family: sans-serif` should be **uncommented** and changed to `font.family : sans-serif`
  * The line `#font.sans-serif` should also be **uncommented** and add the new font 'SimHei' to it. It should be look like the following. 
  ```
  font.family         : sans-serif
  font.sans-serif     : SimHei, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

  ```
* Delete ~/.cache/matplotlib/
  ```bash
  cd ~/.cache/
  rm -rf matplotlib/
  ```
* restart the kernel
* when wanting to use Chinese font, using the following when drawing figures.
  ```python
  import matplotlib.pyplot as plt
  if ifChinese == True:
       plt.rcParams['font.family'] = 'SimHei'
  else:
       plt.rcParams['font.family'] = 'DejaVu Sans'
        
  ```
<div style="text-align: center"><img src="/assets/images/piechart_chinese.png" alt="food pie chart" width="800"/></div>