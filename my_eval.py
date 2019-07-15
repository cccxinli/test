import torch
from torchvision import datasets
from data import data_transforms
from model import Net
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

dataPath = './russian data'
batch_size = 64
# 判断是否使用GPU
if torch.cuda.is_available():
    use_gpu = True
    print("Using GPU")
else:
    use_gpu = False
    print("Using CPU")

FloatTensor = torch.cuda.FloatTensor if use_gpu else torch.FloatTensor
LongTensor = torch.cuda.LongTensor if use_gpu else torch.LongTensor
ByteTensor = torch.cuda.ByteTensor if use_gpu else torch.ByteTensor
Tensor = FloatTensor

test_loader = torch.utils.data.DataLoader(
    datasets.ImageFolder(dataPath + '/val',
                         transform=data_transforms),
    batch_size=batch_size, shuffle=False, num_workers=0, pin_memory=use_gpu)

model = Net()
fc2_infeature = model.fc2.in_features
model.fc2 = nn.Linear(fc2_infeature,20)
model.load_state_dict(torch.load('./model/data_40.pth'))
model.cuda()

import numpy as np
import torchvision

dataiter = iter(test_loader)
images, labels = dataiter.next()
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

for batch_idx, (data, target) in enumerate(test_loader):
    data, target = Variable(data), Variable(target)
    print(data)
    break

#imshow(torchvision.utils.make_grid(images))


# model.eval()  # 设置为验证模式，对Dropout和BatchNorm有影响
# test_loss = 0
# correct = 0
# for data, target in test_loader:
#     with torch.no_grad():
#         data, target = Variable(data), Variable(target)
#         if use_gpu:
#             data = data.cuda()
#             target = target.cuda()
#         output = model(data)
#         test_loss += F.nll_loss(output, target, size_average=False).data.item()  # sum up batch loss
#         # pred = output.data.max(1, keepdim=True)[1]  # get the index of the max log-probability
#         # correct += pred.eq(target.data.view_as(pred)).cpu().sum()
#         max_index = output.max(dim=1)[1]  # 取分类结果，即每行的最大值
#         correct += (max_index == target).sum()  # 准确数计算
#
# test_loss /= len(test_loader.dataset)
#     # scheduler.step(np.around(validation_loss, 2))
# print('\nValidation set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
#     test_loss, correct, len(test_loader.dataset),
#     100. * correct / len(test_loader.dataset)))
