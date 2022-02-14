import os

def rename(dir):
  for folder_name in os.listdir(dir):
    folder_path = os.path.join(dir, folder_name)
    for idx, image_name in enumerate(os.listdir(folder_path)):
      image_path = os.path.join(folder_path, image_name)
      if (idx+1) < 10:
        os.rename(image_path, folder_path + '/' + folder_name + '_0' + str(idx+1) + '.jpg')
      else:
        os.rename(image_path, folder_path + '/' + folder_name + '_' + str(idx+1) + '.jpg')
  print('Done.')

root_dir = '/content/drive/MyDrive/boys_dataset'
rename(os.path.join(root_dir, 'train'))
rename(os.path.join(root_dir, 'val'))

def to_csv(dir):
  i = 0
  # with open('train.csv', 'w') as f:
  with open('val.csv', 'w') as f:
    for folder_name in os.listdir(dir):
      folder_path = os.path.join(dir, folder_name)
      for image_name in os.listdir(folder_path):
        f.write(image_name + ',' + str(i) + '\n')
      i = i + 1
  print('Done.')

to_csv(os.path.join(root_dir, 'train'))
to_csv(os.path.join(root_dir, 'val'))