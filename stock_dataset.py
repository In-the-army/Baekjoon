import pandas as pd
import numpy as np
import os
from torch.utils.data import Dataset

class StockDataset(Dataset):
    def __init__(self, path, code, mode=None, num_val_data=60, num_test_data=60, num_input=10, transform=None, target_transform=None):
        # train or test or validate? 'train', 'test', 'val'
        self.mode = mode
        # the transforms are just for those who need them.
        self.transform = transform
        self.target_transform = target_transform
        # generate the file name.
        fn = os.path.join(str(path), str(code)+".csv")
        # open the file using pandas.
        self.dataframe=pd.read_csv(fn)
        # flip the order of the data.
        self.data=np.flip(self.dataframe.to_numpy(), axis=0)

        # y = f(x),
        # y: predicted close prices
        # x: previous open, high, low, close prices for "num_input" days.
        self.num_data = len(self.data)
        self.num_input = min([int(self.num_data*0.1), num_input])   # clip num_input.
        self.num_test_data = min([int(self.num_data*0.1), num_test_data])   # clip num_test_data.
        self.num_val_data = min([int(self.num_data*0.1), num_val_data]) # clip num_val_data.
        self.num_data -= self.num_input
        self.num_train_data = self.num_data - self.num_test_data - self.num_val_data

        self.train_starting_idx = self.num_input
        self.test_starting_idx = -self.num_test_data
        self.val_starting_idx = -self.num_val_data-self.num_test_data

        # 가격 추출
        self.price = self.data[:, 1:5]
        self.max_price = np.max(self.price)
        # # 일단 필요 없어서 지움.
        # # 날짜 추출
        # self.date = self.data[:, 0]
        # # 거래량 추출
        # self.volume = self.data[:, 5]
        # # code 저장
        # self.code = code

        self.x = []
        self.y = []
        # extract training data
        if mode == "train":
            for i in range(self.num_train_data):
                i_ = i + self.train_starting_idx
                self.x.append(self.price[i_ - self.num_input:i_])
                self.y.append(self.price[i_, 3])
            self.x = np.array(self.x, dtype=np.float32)
            self.y = np.array(self.y, dtype=np.float32)
        elif mode == "test":
            for i in range(self.num_test_data):
                i_ = i + self.test_starting_idx
                self.x.append(self.price[i_ - self.num_input:i_])
                self.y.append(self.price[i_, 3])
            self.x = np.array(self.x, dtype=np.float32)
            self.y = np.array(self.y, dtype=np.float32)
        elif mode == "val":
            for i in range(self.num_val_data):
                i_ = i + self.val_starting_idx
                self.x.append(self.price[i_ - self.num_input:i_])
                self.y.append(self.price[i_, 3])
            self.x = np.array(self.x, dtype=np.float32)
            self.y = np.array(self.y, dtype=np.float32)
        else:
            for i in range(self.num_data):
                i_ = i + self.train_starting_idx
                self.x.append(self.price[i_ - self.num_input:i_])
                self.y.append(self.price[i_, 3])
            self.x = np.array(self.x, dtype=np.float32)
            self.y = np.array(self.y, dtype=np.float32)

    def __len__(self):
        # 데이터의 길이는?
        if self.mode == "train":
            return self.num_train_data
        elif self.mode == "test":
            return self.num_test_data
        elif self.mode == "val":
            return self.num_val_data
        else:
            return self.num_data

    def __getitem__(self, item):
        # map style의 데이터 접근 방식 제공
        return self.x[item], self.y[item]

if __name__=="__main__":
    path = "./"    # 종목 파일이 들어 있는 폴더의 위치
    code = "122630"         # 종목 코드
    num_val_data = 10
    num_test_data = 10
    num_input = 10
    sd_train = StockDataset(path, code, "train", num_val_data=num_val_data, num_test_data=num_test_data, num_input=num_input)
    sd_val = StockDataset(path, code, "val", num_val_data=num_val_data, num_test_data=num_test_data, num_input=num_input)
    sd_test = StockDataset(path, code, "test", num_val_data=num_val_data, num_test_data=num_test_data, num_input=num_input)

    print(sd_train[0][0])
    print(sd_val[0][0])
    print(sd_test[0][0])

    print(sd_train[0:2])
    print(sd_val[0:2])
    print(sd_test[0:2])

    print(sd_train.max_price)

