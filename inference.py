# import torch
import torch.nn as nn
import numpy as np
# import torch.nn.functional as F
#
# # Neural Network and Optimizer
from model import Net
from data import data_transforms,data_jitter_hue,data_jitter_brightness,data_jitter_saturation,data_jitter_contrast,data_rotate,data_hvflip,data_shear,data_translate,data_center,data_grayscale

# model = Net()
# fc2_features = model.fc2.in_features
# model.fc2 = nn.Linear(fc2_features, 2)
# model.load_state_dict(torch.load('./model/temporary_40.pth'))


import argparse
# from tqdm import tqdm
import os
import PIL.Image as Image

import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torchvision.datasets as datasets
import numpy as np
import time

print('- - - - - - step3 Class inference Begin - - - - - - ')
start = time.time()
model_class = Net()
fc2_features = model_class.fc2.in_features
model_class.fc2 = nn.Linear(fc2_features, 121)
model_class.load_state_dict(torch.load('./new model/class_121.pth'))

model_data = Net()
fc2_features = model_data.fc2.in_features
model_data.fc2 = nn.Linear(fc2_features, 20)
model_data.load_state_dict(torch.load('./new model/data_20.pth'))

def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')

transforms = [data_transforms,data_jitter_hue,data_jitter_brightness,data_jitter_saturation,data_jitter_contrast,data_rotate,data_hvflip,data_shear,data_translate,data_center]

output_file = open('./out.tsv', "w")
output_file.write("frame,xtl,ytl,xbr,ybr,class,temporary,data\n".replace(',','\t'))
test_dir = './test'

# label dict
dataset_class = os.listdir('./rus data//train/')    # classfolder
dataset_class.sort()
class_dict = {}
for i in range(len(dataset_class)):
    class_dict[i] = dataset_class[i]
dataset_data = os.listdir('./rus data//train/')     # datafolder
dataset_data.sort()
data_dict = {}
for i in range(len(dataset_data)):
    data_dict[i] = dataset_data[i]

for f in (os.listdir(test_dir)):
    if 'jpg' in f:
        output_class = torch.zeros([1, 121], dtype=torch.float32)
        output_data = torch.zeros([1, 20], dtype=torch.float32)
        with torch.no_grad():
            for i in range(0,len(transforms)):
                data = transforms[i](pil_loader(test_dir + '/' + f))
                data = data.view(1, data.size(0), data.size(1), data.size(2))
                data = Variable(data)
                output_class = output_class.add(model_class(data))
                output_data = output_data.add(model_data(data))
            pred_class = output_class.data.max(1, keepdim=True)[1]
            pred_data = output_data.data.max(1, keepdim=True)[1]
            imgName = f.split('_')[-1]
            xtl = f.split('_')[0]
            ytl = f.split('_')[1]
            xbr = f.split('_')[2]
            ybr = f.split('_')[3]
            output_file.write("%s,%s,%s,%s,%s,%s\n".replace(',','\t') % (imgName,xtl,ytl,xbr,ybr, label_trans[int(pred)]))

output_file.close()
end = time.time()
print('outfile saved in /root/chenxinli/out.csv')
print('=> step3 time cost {:.2f} s'.format(end-start) )
print('- - - - - - step3 Class inference Down - - - - - -')
print('\n')