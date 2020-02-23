""" Train and Test Models """

from pytroch_models import NN3Layer, NN4Layer, CNN3Layer, CNN5Layer
from load_data import DataLoader
import torch

# train & test parameters
epochs = 100
learning_rate = 0.01
verbose = 200

# model parameters
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NN3Layer().to(device)
criterion = torch.nn.MSELoss()#CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
output_path = 'outputs/NN3Layer.torch'

# data loader
goog_dl = DataLoader(
    path = 'data/original/GOOG_history.csv',
    x_attributes=['Open','Close','High','Low'],
    y_attributes=['Close'],
    x_days = 3,
    y_days = 1,
    step = 1,
    train_frac = 2/3)
goog_train_l,goog_test_l = goog_dl.get_loaders()

# train and test model
for epoch in range(epochs):
    # Train
    for i, (x, y) in enumerate(goog_train_l()):
        x = torch.tensor(x,dtype=torch.float32).to(device)
        y = torch.tensor(y,dtype=torch.float32).to(device)  
        # forward pass
        y_hat = model(x.view(-1,12))
        loss = criterion(y_hat,y)
        # backward propogation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if i!= 0 and (i+1)%verbose==0:
            print ('Epoch %-10d Batch %-10d Loss %-10.4f'%(epoch+1, i+1, loss.item()))
    # Test
    with torch.no_grad():
        total_loss = 0
        for i,(x,y) in enumerate(goog_test_l()):
            x = torch.tensor(x,dtype=torch.float32).to(device)
            y = torch.tensor(y,dtype=torch.float32).to(device)
            y_hat = model(x.view(-1,12))
            total_loss += criterion(y_hat,y).item()
    print('Average Test Accuracy: %.4f'%(total_loss/i))

# Save the model checkpoint
torch.save(model,output_path)
