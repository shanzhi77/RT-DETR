import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('')
    model.val(data='',
              split='tset',
              imgsz=640,
              batch=16,
            #   save_json=True, # if you need to cal coco metrice
              project='runs/test',
              name='exp',
              )