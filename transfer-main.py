from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import numpy as np

# 参数设置
dataPath = './data'
batch_size = 64
epochs = 40
lr = 0.0001
seed = 1  # 随机种子
log_interval = 10  # 间隔10个batch输出一次信息

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

# 数据集制作
from data import initialize_data, data_transforms, data_jitter_hue, data_jitter_brightness, data_jitter_saturation, \
    data_jitter_contrast, data_rotate, data_hvflip, data_shear, data_translate, data_center, data_hflip, \
    data_vflip  # data.py in the same folder

# 数据增强:十倍,用concatdataset链接各个数据集
train_loader = torch.utils.data.DataLoader(
    torch.utils.data.ConcatDataset([datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_transforms),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_jitter_brightness),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_jitter_hue),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_jitter_contrast),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_jitter_saturation),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_translate),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_rotate),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_hvflip),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_center),
                                    datasets.ImageFolder(dataPath + '/train',
                                                         transform=data_shear)]), batch_size=batch_size, shuffle=True,
    num_workers=0, pin_memory=use_gpu)

# 验证集不增强
val_loader = torch.utils.data.DataLoader(
    datasets.ImageFolder(dataPath + '/val',
                         transform=data_transforms),
    batch_size=batch_size, shuffle=False, num_workers=0, pin_memory=use_gpu)

# 神经网络和优化器
from model import Net

model = Net()
model_dict=model.load_state_dict(torch.load('./model/40.pth'))
fc2_infeature = model.fc2.in_features
model.fc2 = nn.Linear(fc2_infeature,4)


if use_gpu:
    model.cuda()

# 优化器和学习率变化策略设置
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=lr)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=5, factor=0.5, verbose=True)


def train(epoch):
    model.train()  # 设置为训练模式，对Dropout和BatchNorm有影响
    correct = 0
    training_loss = 0
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        if use_gpu:
            data = data.cuda()
            target = target.cuda()
        optimizer.zero_grad()  # 将网络中的所有梯度置0
        output = model(data)
        loss = F.nll_loss(output, target)  # nll_loss和log_softmax搭配使用，输入是对数概率向量和目标标签
        loss.backward()  # 反向传播
        optimizer.step()
        max_index = output.max(dim=1)[1]  # 取分类结果，即每行的最大值
        correct += (max_index == target).sum()  # 准确数计算
        training_loss += loss
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss per example: {:.6f}\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.data.item() / (batch_size * log_interval),
                loss.data.item()))
    print('\nTraining set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        training_loss / len(train_loader.dataset), correct, len(train_loader.dataset),
        100. * correct / len(train_loader.dataset)))


def validation():
    model.eval()  # 设置为验证模式，对Dropout和BatchNorm有影响
    validation_loss = 0
    correct = 0
    for data, target in val_loader:
        with torch.no_grad():
            data, target = Variable(data), Variable(target)
            if use_gpu:
                data = data.cuda()
                target = target.cuda()
            output = model(data)
            validation_loss += F.nll_loss(output, target, size_average=False).data.item()  # sum up batch loss
            pred = output.data.max(1, keepdim=True)[1]  # get the index of the max log-probability
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    validation_loss /= len(val_loader.dataset)
    scheduler.step(np.around(validation_loss, 2))
    print('\nValidation set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        validation_loss, correct, len(val_loader.dataset),
        100. * correct / len(val_loader.dataset)))


for epoch in range(1, epochs + 1):
    train(epoch)
    validation()
    model_file = 'model_' + str(epoch) + '.pth'
    torch.save(model.state_dict(), model_file)
