import torch
from torch import nn
from torch.utils.data import DataLoader
from stock_dataset import StockDataset
import numpy as np
import copy

batch_size = 32
num_input = 20
num_test = 1
num_val = 60

# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

# Define model
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.Sequential(
            nn.Linear(4*num_input, 1)
        )

    def forward(self, x):
        x = self.flatten(x)
        #print(x.shape)
        logits = self.linear(x)
        #print(logits.shape)
        return logits.flatten()

class LSTMModel(nn.Module):
    def __init__(self):
        super(LSTMModel, self).__init__()
        pass

    def forward(self, x):
        pass

def train(dataloader, model, loss_fn, optimizer, max_price):
    size = len(dataloader.dataset)
    model.train()
    mean_loss = 0
    count_loss = 0
    for batch, (X, y) in enumerate(dataloader):
        X_ = X/max_price
        #print(X.shape)
        y_ = y/max_price
        #print(y.shape)
        X_, y_ = X_.to(device), y_.to(device)

        # Compute prediction error
        pred = model(X_)
        loss = loss_fn(pred, y_)#y.reshape((-1,1)))

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        mean_loss += loss.item()
        count_loss += len(X)

    mean_loss /= count_loss
    print(f"mean loss: {mean_loss:>7f}")

def test(dataloader, model, loss_fn, max_price, mode='val'):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss = 0
    count_test = 0
    with torch.no_grad():
        for X, y in dataloader:
            X_ = X / max_price
            y_ = y / max_price
            X_, y_ = X_.to(device), y_.to(device)
            pred = model(X_)
            test_loss += loss_fn(pred, y_).item()#.reshape(-1,1)).item()
            count_test += len(X)
    test_loss /= count_test
    test_loss = max_price*np.sqrt(test_loss)
    if mode == 'val':
        print(f"Validation RMSE: {test_loss:>7f} \n")
    else:
        print(f"Test RMSE: {test_loss:>7f} \n")

    return test_loss

# for t in range(num_repeat):
#     np.random.seed(t)
#     tf.random.set_seed(t)

path = "./"    # 종목 파일이 들어 있는 폴더의 위치
code = "122630"         # 종목 코드
sd_train = StockDataset(path, code, "train", num_input=num_input, num_val_data=num_val, num_test_data=num_test)
sd_val = StockDataset(path, code, "val", num_input=num_input, num_val_data=num_val, num_test_data=num_test)
sd_test = StockDataset(path, code, "test", num_input=num_input, num_val_data=num_val, num_test_data=num_test)

train_dataloader = DataLoader(sd_train, batch_size=batch_size)
val_dataloader = DataLoader(sd_val, batch_size=batch_size)
test_dataloader = DataLoader(sd_test, batch_size=batch_size)

epochs = 1000
max_tolerance = 100
N=10

tolerance = 0
best_val_loss = np.finfo(float).max
best_model = None
model = LinearModel().to(device)
loss_fn = nn.MSELoss(reduction="sum")
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer, sd_train.max_price)
    val_loss = test(val_dataloader, model, loss_fn, sd_train.max_price)
    if val_loss > best_val_loss:
        if tolerance > max_tolerance:
            break
        else:
            tolerance += 1
    else:
        best_val_loss = val_loss
        best_model=copy.deepcopy(model)
path = './model.pt'
torch.save(best_model, path)
print("Done!")

y_gt=0
y_pred=[]
y_pred_lstm=[]

path = './model.pt'
net = torch.load(path)

loss_fn = nn.MSELoss(reduction="sum")
test_loss = test(test_dataloader, net, loss_fn, sd_train.max_price, mode='test')

X, y_gt_ = sd_test[0:]
X_ = X / sd_train.max_price
X_ = torch.Tensor(X_).to(device)
y = net(X_)
y_gt = y_gt_[0]
y_pred.append((y*sd_train.max_price).detach().numpy()[0])

print(y_pred)
print(y_gt)
