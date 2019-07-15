import json
import os
import cv2

f = open('training_seq.json', encoding='utf-8')
data = json.loads(f.read())
srcPathRoot = '../russ pic/pic total/'
savePathRoot = './total-tempopary/train/'
# k = 1
# for i in range(len(data)):
#     imageName = data[i]['image_name']
#     srcPath = srcPathRoot + imageName
#     boxes = data[i]['bboxes']
#     for j in range(len(boxes)):
#         #folderName = data[i]['temporary'][j]
#         # print(folderName)
#         # break
#         if data[i]['data'][j] != '':
#             folderName =  data[i]['data'][j].replace(':', '.')
#         else:
#             folderName = 'not_data'
#         savePath = savePathRoot + folderName
#         if not os.path.exists(savePath):
#             os.makedirs(savePath)  # 创建路径
#         xtl = int(boxes[j][0])  # 从文件中获取框信息，float型转int出错？直接用分割获取整数部分
#         ytl = int(boxes[j][1])
#         xbr = int(boxes[j][2])
#         ybr = int(boxes[j][3])
#         if (xbr - xtl) * (ybr - ytl) < 100:
#             continue
#         img = cv2.imread(srcPath)
#         crop = img[ytl:ybr, xtl:xbr]  # 裁剪图片[左上y：右下y，左上x：右下x]
#         cropImgPath = savePath + '/' + str(k).zfill(6) + '.jpg'
#         cv2.imwrite(cropImgPath, crop)  # 保存裁剪图
#         print('the %dth pic ' % (k))
#         k += 1

    # if k ==10:
    #     break


f = open('test_seq.json', encoding='utf-8')
data = json.loads(f.read())
srcPathRoot = '../russ pic/pic total/'
savePathRoot = './total-data/train/'
k = 13277
for i in range(len(data)):
    imageName = data[i]['img_name']
    srcPath = srcPathRoot + imageName
    boxes = data[i]['bboxes']

    #folderName = data[i]['class']
    if data[i]['data'] != '':
        folderName = data[i]['data'].replace(':', '.')
    else:
        folderName = 'not_data'
    savePath = savePathRoot + folderName
    if not os.path.exists(savePath):
        os.makedirs(savePath)  # 创建路径
    xtl = int(boxes[0])        # 从文件中获取框信息，float型转int出错？直接用分割获取整数部分
    ytl = int(boxes[1])
    xbr = int(boxes[2])
    ybr = int(boxes[3])
    if (xbr - xtl) * (ybr - ytl) < 100:
        continue
    img = cv2.imread(srcPath)
    crop = img[ytl:ybr, xtl:xbr]  # 裁剪图片[左上y：右下y，左上x：右下x]
    cropImgPath = savePath + '/' + str(k).zfill(6) + '.jpg'
    cv2.imwrite(cropImgPath, crop)  # 保存裁剪图
    print('the %dth pic ' % (k))
    k += 1
    # if k ==13287:
    #     break