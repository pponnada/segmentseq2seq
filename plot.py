import matplotlib.pyplot as plt


def plot_frequencies(freq_map, max_freq, xlabel, ylabel, title, fname):
  lists = sorted(freq_map.items())
  x, y = zip(*lists)
  plt.figure(figsize=(6, 6))
  plt.plot(x, y)
  plt.ylim(0, max_freq)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.savefig(fname)
  print("saved blocks plot as {}".format(fname))

def plot_predictions(lbls, preds, segment_size, min_block_freq, max_win_ms):
  lbls_max = lbls.max()
  lbls_min = lbls.min()
  plt.ylim(lbls_min, lbls_max)
  f = plt.figure(figsize=(10, 10), dpi=120)
  ax = f.add_subplot(111)
  plt.plot(preds, 'g--', lbls, 'r--')
  text = 'segment size: ' + str(segment_size) + ', min block freq: ' +  str(min_block_freq) + ', max access win: ' + str(max_win_ms)
  plt.text(0.45, 0.95, text, ha='center', va='center', transform=ax.transAxes)
  plt.yticks([lbls_min, (lbls_min + lbls_max)/2, lbls_max])
  plt.xlabel('batched test data')
  plt.ylabel('segment offset')

  plt.title("Segment prediction")
  plt.legend(['preds', 'labels'])

  fname = 'predict-'+str(segment_size)+'freq-'+str(min_block_freq)+'win-'+str(max_win_ms)+".png"
  plt.savefig(fname)
  print("Saved plot as: {}".format(fname))


