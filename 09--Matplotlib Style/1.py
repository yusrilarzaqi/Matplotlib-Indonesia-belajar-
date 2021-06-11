import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def gambar_barplot():
  data = [25, 45, 55, 125, 225]
  kategori = ['A', 'B', 'C', 'D', 'E']
  
  # Pengaturan Grid Dan Color
  plt.bar(kategori, data,
          color = 'red',
          alpha = .25)
  
  plt.grid(linestyle = '--',
           linewidth=2,
           axis = 'y',
           alpha = .5
           )
  
  plt.xlabel('Katrgori')
  plt.ylabel('Jumlah')
  plt.title('Contoh Bar Plot')
  plt.show()

style.use('ggplot')
gambar_barplot()
