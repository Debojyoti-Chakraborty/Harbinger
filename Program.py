import sys
import math


def main():
    input_from_file()


# This method returns the value after using the sigmoid activation.
def sigmoid(x, derivative):
    if not derivative:
        return 1/(1 + math.exp(-x))
    else:
        return sigmoid(x, False) * (1 - sigmoid(x, False))


def error(target, output):
    error_value = 0.5 * math.pow((target - output), 2)
    return error_value


def update_weights(target, output, weights, inputs):
    for i in range(0, len(weights) - 1):
        while math.fabs(error(target, output)) > 0.01:
            dw = inputs[i] * (target - output) * (1 - output)
            weights[i] = weights[i] - dw

    return weights


def forward_propagation(data_max, data_min, weights):
    output_data = []
    for i in range(0, len(data_max) - 1):
        output = sigmoid(data_max[i] * weights[0] + data_min[i] * weights[1], False)
        output_data.append(output)
        target = data_max[i+1]
        inputs = [data_max[i], data_min[i]]
        weights = update_weights(target, output, weights, inputs)


# This method returns the normalised values of the maximum and minimum temperatures.
def normalisation(x):
    x_max = float(max(x))
    x_min = float(min(x))
    n = len(x)
    x_n = []
    for i in range(0, n-1):
        x_n.append((float(x[i]) - float(x_min)) / (float(x_max) - float(x_min)))

    return x_n

    
# This method inputs data from file into lists
def input_from_file():
    file_to_open = "book1.txt"
    f = open(file_to_open, "r")
    lines = f.readlines()
    min_temp = []
    max_temp = []
    # x.split()[1] refers to data in second column
    for x in lines:
        max_temp.append(float(x.split('\t')[2]))
        min_temp.append(float(x.split('\t')[3].replace("\n", "")))
    f.close()
    first_10_values_min = min_temp[1:11]
    first_10_values_max = max_temp[1:11]
    n_max = normalisation(first_10_values_max)
    n_min = normalisation(first_10_values_min)
    print(n_max)
    print(n_min)


if __name__ == "__main__":
    sys.exit(main())
