# Define de model and the layers
from tensorflow.keras.models import Sequential # Simplest model instead of customized
from tensorflow.keras.layers import Dense # All perceptrons are connected
from tensorflow.keras.layers import LSTM # All perceptrons are connected

#from tensorflow.keras.layers import Conv2D 
#from tensorflow.keras.layers import Conv1D 
#from tensorflow.keras.layers import MaxPool2D
#from tensorflow.keras.layers import Flatten
#from tensorflow.keras.layers import MaxPool1D
from tensorflow.keras.layers import Dropout
#from tensorflow.keras.layers import Input

from tensorflow.keras.optimizers import Adam

class TrainTestModel(Sequential):
    
    def __init__(self, dim0, dim1, layers=None, name=None):
        super().__init__(layers=layers, name=name)

        #model = Sequential()
        self.add(Dense(96, input_shape = (dim0, dim1), activation = 'relu'))
        #model.add(Dense(100, input_shape = (96, 1), activation = 'relu'))
        #model.add(LSTM(200, activation='tanh', dropout=0.2, return_sequences=True))
        self.add(LSTM(200, activation='tanh', dropout=0.3))
        #model.add(Dense(50, activation='relu'))
        #model.add(Dropout(0.3))
        #model.add(Dense(100, activation='relu'))
        #model.add(Dropout(0.1))
        self.add(Dense(1, activation='linear'))
        self.summary()

    def train_model(self, X_train, y_train, X_test, y_test, ep, bs):
        adam = Adam(lr=0.0001)
        self.compile(optimizer=adam, loss='mean_squared_error')
        self.fit(X_train, y_train, epochs=ep, batch_size=bs, validation_data=(X_test, y_test), verbose = 1, shuffle=False)
        #return self.model
