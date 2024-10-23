#class for aihub dataset handling
# '/Users/cha/DATASET/168.한국 전통 수묵화 화풍별 제작 데이터'

import zipfile
import os
import glob
from tqdm import tqdm

class aihubdata:
    def __init__(self, path=None):
        self.path = path
        
    def treeview(self, path=None, n=0, onlydir = True):
        if not path:
            path = self.path
        
        for i in sorted(os.listdir(path)):   
            i_path = os.path.join(path, i)
            if os.path.isdir(i_path):
                print('\t'*n, i, ':', len(os.listdir(i_path)))
                self.treeview(os.path.join(i_path), n+1, onlydir=onlydir)
            else:
                if not onlydir:
                    print('\t'*n, i)
                    
    def unzip(self): 
        zip_list = os.listdir(self.path)
        dir_list = []
        for file_name in zip_list:
            dir_list.append(file_name.split('_')[-4] + '_' + file_name.split('_')[-2][-3] + '_' + file_name.split('_')[-1][0])

        dir_list.sort()
        for i in tqdm(dir_list):
            if i == 'L01_1_A' or 'L02_1_A':
                pass
            os.makedirs(OUTPUT_PATH + i, exist_ok = True)
            os.makedirs(OUTPUT_PATH + i + '/images', exist_ok = True)

            zip_file = zipfile.ZipFile(PATH + file_name)
            zip_file.extractall(path=OUTPUT_PATH + i + '/images/')

        print('complete')
