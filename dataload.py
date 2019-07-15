import cv2

file = 'GroundTruth.txt'
i = 1
with open(file, 'r') as f:                           # 读文件
    for line in f:                                   # 一行一行读取
        a = line.split(';')                          # 每行用分号分割
        imgPath = 'E:/BaiduNetdiskDownload/0/all-jpg/' + a[0].split('.')[0] + '.jpg'   # 获取每行图片名，补全图片路径
        savePath = './data/train/' + a[5].rstrip() + '/' + str(i).zfill(6) + '.jpg'    # 设置裁剪后的保存路径
        img = cv2.imread(imgPath)                    # 用opencv读图
        # print(a[0],a[1], a[2],a[3],a[4],a[5])
        lty = int(a[2].split('.')[0])                # 从文件中获取框信息，float型转int出错？直接用分割获取整数部分
        bry = int(a[4].split('.')[0])
        ltx = int(a[1].split('.')[0])
        brx = int(a[3].split('.')[0])
        # print(imgPath)
        # print(savePath)
        crop = img[lty:bry, ltx:brx]                 # 裁剪图片[左上y：右下y，左上x：右下x]
        cv2.imwrite(savePath, crop)                  # 保存裁剪图
        print('the {}th pic processed'.format(i))
        i = i + 1



