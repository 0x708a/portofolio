import numpy as np

class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)
        self.synaptic_wheights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        for i in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_wheights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_wheights))

        return output


if __name__ == "__main__":
    net = NeuralNetwork()
    print("Random weights: " + str(net.synaptic_wheights))

    training_inputs = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    net.train(training_inputs, training_outputs, 10000)

    print("Wheights after training: " + str(net.synaptic_wheights))

    a = str(input("Input 1: "))
    b = str(input("Input 2: "))
    c = str(input("Input 3: "))

    print("New Situation, data = ", a, b, c)
    print("Output data: ")
    print(net.think(np.array([a, b, c])))
