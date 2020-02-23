""" Models built with PyTroch """

import torch


class NN3Layer(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(
            in_features = 12,
            out_features = 5) 
        self.activ1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(
            in_features = 5,
            out_features = 1)  
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.activ1(x)
        x = self.fc2(x)
        return x


class NN4Layer(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(
            in_features = 100,
            out_features = 50) 
        self.activ1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(
            in_features = 50,
            out_features = 25) 
        self.activ2 = torch.nn.ReLU()
        self.fc3 = torch.nn.Linear(
            in_features = 25,
            out_features = 2)  
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.activ1(x)
        x = self.fc2(x)
        x = self.activ2(x)
        x = self.fc3(x)
        return x


class CNN3Layer(torch.nn.Module):
    
    def __init__(self):
        self.conv1 = torch.nn.Conv2d(
            in_channels = 1,
            out_channels = 5,
            kernel_size = 2,
            stride = 1,
            padding=1)
        self.activ1 = torch.nn.ReLu()
        self.pool1 = torch.nn.MaxPool2d(
            kernel_size = 2,
            stride = 2,
            padding = 0)
        self.activ2 = torch.nn.ReLu()
        self.fc1 = torch.nn.Linear(
            in_features = 5*16*16,
            out_features = 2)
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.activ1(x)        
        x = self.pool1(x)        
        x = self.activ2(x)
        x = self.fc1(x.view(-1,5*16*16))
        return(x)


class CNN5Layer(torch.nn.Module):
    
    def __init__(self):
        self.conv1 = torch.nn.Conv2d(
            in_channels = 1,
            out_channels = 5,
            kernel_size = 2,
            stride = 1,
            padding = 1)
        self.activ1 = torch.nn.ReLu()
        self.pool1 = torch.nn.MaxPool2d(
            kernel_size = 2,
            stride = 2,
            padding = 0)
        self.activ2 = torch.nn.ReLu()
        self.conv2 = torch.nn.Conv2d(
            in_channels = 1,
            out_channels = 5,
            kernel_size = 2,
            stride = 1,
            padding = 1)
        self.activ2 = torch.nn.ReLu()
        self.pool2 = torch.nn.MaxPool2d(
            kernel_size = 2,
            stride = 2,
            padding = 0)
        self.activ3 = torch.nn.ReLu()
        self.fc1 = torch.nn.Linear(
            in_features = 5*16*16,
            out_features = 2)
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.activ1(x)        
        x = self.pool1(x)        
        x = self.activ2(x)
        x = self.conv2(x)
        x = self.activ2(x)
        x = self.pool2(x)
        x = self.activ3(x)
        x = self.fc1(x.view(-1,5*16*16))
        return(x)