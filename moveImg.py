import os,shutil
import random
def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):           #判断文件是否存在
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print ("move %s -> %s"%( srcfile,dstfile))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):           #判断文件是否存在
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print ("copy %s -> %s"%( srcfile,dstfile))

srcDirRoot = './rus data-100/train/'
dstDirRoot = './rus data-100/val/'
list = os.listdir(srcDirRoot)  # 列出文件夹下所有的目录名与文件名，不包含二级文件
print(list)
for i in range(0, len(list)):
    srcPath = srcDirRoot + list[i]
    dstDir = dstDirRoot + list[i]
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)            # 创建路径
    imgList = os.listdir(srcPath)
    for j in range(len(imgList)):
        srcImgPath = os.path.join(srcPath,imgList[j])
        dstImgPath = os.path.join(dstDir,imgList[j])
        #print(len(imgList))
        #print(srcImgPath, valImgPath)
        mycopyfile(srcImgPath, dstImgPath)
        j += 1
    # imgList = os.listdir(valDir)
    # for j in range(len(imgList)):
    #     srcImgPath = os.path.join(srcPath, imgList[j])
    #     valImgPath = os.path.join(valDir, imgList[j])
    #     mymovefile(valImgPath, srcImgPath)
    #     j += 1
    i += 1
    # if i == 2:
    #     break

