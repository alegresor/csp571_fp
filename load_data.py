""" Data Loader """

import pandas as pd

class DataLoader(object):

    def __init__(self, path, x_attributes, y_attributes, x_days, y_days, step, train_frac):
        """
        Args:
            path (str): path to DataFrame
            x_attributes (list): list of attributes for observation
            y_attributes (list): list of attributes for label
            x_days (int): number of days of data to return as observation
            y_days (int): number of days of data to return as label
            step (int): number of days to window
            train_frac (float): fraction of data to use for training
        """
        self.path = path
        self.x_attributes = x_attributes
        self.y_attributes = y_attributes
        self.x_days = x_days
        self.y_days = y_days
        self.step = step
        self.train_frac = train_frac
        df = pd.read_csv(path)
        self.x_vals = df[self.x_attributes].values
        self.y_vals = df[self.y_attributes].values
        n = (len(df)-self.y_days-self.x_days)//self.step
        self.n_train = int(n*self.train_frac)
        self.n_test = n-self.n_train
    
    def get_loaders(self):
        def train_loader():
            for i in range(self.n_train):
                day_start = i*self.step
                day_split = day_start+self.x_days
                day_end = day_split+self.y_days
                x = self.x_vals[day_start:day_split]
                y = self.y_vals[day_split:day_end]
                yield x,y
        def test_loader():
            base_day = (self.n_train)*self.step
            for i in range(self.n_test):
                day_start = base_day+self.step*i
                day_split = day_start+self.x_days
                day_end = day_split+self.y_days
                x = self.x_vals[day_start:day_split]
                y = self.y_vals[day_split:day_end]
                yield x,y
        return train_loader,test_loader
    
# Example with GOOG data
goog_dl = DataLoader(
    path = 'data/original/GOOG_history.csv',
    x_attributes=['Date','Open'],
    y_attributes=['Date','Close'],
    x_days = 5,
    y_days = 2,
    step = 3,
    train_frac=2/3)
goog_train_l,goog_test_l = goog_dl.get_loaders()

for i,(x,y) in enumerate(goog_train_l()):
    pass
    print('Train x_%d \t%s\n\t%s'%(i,str(x.shape),str(x).replace('\n','\n\t')))
    print('Train y_%d \t%s\n\t%s\n'%(i,str(y.shape),str(y).replace('\n','\n\t')))

print('~'*100)

for i,(x,y) in enumerate(goog_test_l()):
    print('Test x_%d \t%s\n\t%s'%(i,str(x.shape),str(x).replace('\n','\n\t')))
    print('Test y_%d \t%s\n\t%s\n'%(i,str(y.shape),str(y).replace('\n','\n\t')))
    if i>10:
        break



