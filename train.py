import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('/hy-tmp/RTDETR-long/ultralytics/cfg/models/rt-detr/rtdetr-RGCSPELAN-Light-EHE.yaml')#t
    # model.load('') # loading pretrain weights
    model.train(data='/hy-tmp/data.yaml',
                cache=False,#False
                imgsz=640,
                epochs=1000,
                patience=10,
                batch=1,
                workers=2,
                device='0',
                # resume='', # last.pt path
                project='runs/train',
                name='rtdetr',

                )
#E:\PycharmProjects\RTDETR\RTDETR\ultralytics