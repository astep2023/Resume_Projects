import numpy as np
import time

'''
Name: Amir Stephens
CWID: A20439928
UID: astephens
email: astephens@hawk.iit.edu
'''

class Perceptron:
    def __init__(self, learning_rate: float, iters: int) -> None:
        self.learning_rate: float = learning_rate
        self.iters: int = iters
        self.samples: int = 0
        self.features: int = 0
        self.weights: float = list()
        self.bias: float = 0

    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        self.features: int = X.shape[1]
        self.weights: float = [0 for _ in range(self.features)]

        for _ in range(self.iters):
            for i, x in enumerate(X):
                predicted: int = self.predict(x)

                if not Y[i] == predicted:
                    self.weights += self.learning_rate * Y[i] * x
                    self.bias += self.learning_rate * Y[i]

    def predict(self, X: np.ndarray) -> int:
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted: int = self.activation_function(linear_output)
        return y_predicted

    def activation_function(self, x) -> int:
        if isinstance(x, np.ndarray):
            guess: int = [0 for _ in range(len(x))]
            for i in range(len(x)):
                if x[i] >= 0:
                    guess[i] = 1
                else:
                    guess[i] = -1
            return guess
        else:
            if x >= 0:
                return 1
            else:
                return -1
            
    def metrics(self, predictions) -> int:
        correct = 0
        wrong = 0
        for i, prediction in enumerate(predictions):
            if prediction == Y[i]:
                correct += 1
            else:
                wrong += 1
        return correct, wrong

if __name__ == "__main__":
    # Part A.
    samples: int = 100 
    learning_rate: int = 1 
    mean_1: float = [0.5, 0.5] 
    mean_2: float = [-0.5, -0.5] 
    variance: float = 0.1  
    std: float = np.sqrt(variance) 
    
    # Generate random data
    data_1: float = np.random.normal(mean_1[0], std, samples)
    data_2: float = np.random.normal(mean_1[1], std, samples)
    data_1b:float = np.random.normal(mean_2[0], std, samples)
    data_2b:float = np.random.normal(mean_2[1], std, samples)

    # Combine the data.
    data1: np.ndarray = np.array([[x1, x2] for x1, x2 in zip(data_1, data_2)])
    data2: np.ndarray = np.array([[x1, x2] for x1, x2 in zip(data_1b, data_2b)])

    # Labels for the data
    labels_1: int = [1 for _ in range(samples)]
    labels_2: int = [-1 for _ in range(samples)]

    # Combines the lists & Convert the combined lists
    X: np.ndarray = np.array([*data1, *data2])
    Y: np.ndarray = np.array([*labels_1, *labels_2])

    #Part B.
    # Initialize and train the Perceptron
    perceptron: Perceptron = Perceptron(learning_rate, samples)
    perceptron.train(X, Y)

    # Test predictions
    start: float = time.time()
    predictions: int = perceptron.predict(X)
    stop: float = time.time()
    length: float = stop - start
    correct, wrong = perceptron.metrics(predictions)

    print("X:", X)
    print("Y:", Y)
    print("predictions:", predictions)
    print("It took: ", length)
    print("Right", correct)
    print("Wrong", wrong)

    #Part C.
    #second dataset
    variance: float = .8  # Variance of the Gaussian distribution

    # Generate data for two classes with Gaussian distributions
    std: float = np.sqrt(variance)

    # Generate random data
    data_3: float = np.random.normal(mean_1[0], std, samples)
    data_4: float = np.random.normal(mean_1[1], std, samples)
    data_3b:float = np.random.normal(mean_2[0], std, samples)
    data_4b:float = np.random.normal(mean_2[1], std, samples)

    data3: np.ndarray = np.array([[x1, x2] for x1, x2 in zip(data_3, data_4)])
    data4: np.ndarray = np.array([[x1, x2] for x1, x2 in zip(data_3b, data_4b)])

    X2: np.ndarray = np.array([*data3, *data4])

    perceptron.train(X2,Y)
    start: float = time.time()
    second_predictions: int = perceptron.predict(X2)
    stop: float = time.time()
    length: float = stop - start
    correct, wrong = perceptron.metrics(second_predictions)
    
    print("X:", X2)
    print("second predictions:", second_predictions)
    print("It took: ", length)
    print("Right", correct)
    print("Wrong", wrong)