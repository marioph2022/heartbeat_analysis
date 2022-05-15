import numpy as np


class TrainTestData:

    def split_barcode_data(self, tda_repr, y_data, window_size):
        X = []
        y = []
        for idx in range(0, tda_repr.shape[0] - 1):
            X.append(tda_repr[idx])
            y.append(y_data[idx + window_size])

        X = np.array(X)
        y = np.array(y)

        # This is the split of one month of data
        return X[:2112], y[:2112], X[2112:], y[2112:]