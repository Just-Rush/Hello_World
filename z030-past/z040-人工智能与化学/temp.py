import numpy as np
import matplotlib.pyplot as plt


# 激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# 初始化权重和偏置
np.random.seed(42)
input_size = 1
hidden_size = 10  # 增加隐藏层节点数量
output_size = 1

weights_input_hidden = np.random.randn(input_size, hidden_size) * np.sqrt(2 / input_size)  # Xavier初始化
bias_hidden = np.zeros((1, hidden_size))
weights_hidden_output = np.random.randn(hidden_size, output_size) * np.sqrt(2 / hidden_size)  # Xavier初始化
bias_output = np.zeros((1, output_size))

# 学习率
learning_rate = 0.01

# 训练数据
X_train = np.array([[-10], [-8], [-6], [-4], [-2], [0], [2], [4], [6], [8], [10]])
y_train = np.abs(X_train)


# 前向传播
def forward_propagation(X):
    z_hidden = np.dot(X, weights_input_hidden) + bias_hidden
    a_hidden = sigmoid(z_hidden)
    z_output = np.dot(a_hidden, weights_hidden_output) + bias_output
    y_pred = z_output
    return z_hidden, a_hidden, z_output, y_pred


# 反向传播
def backward_propagation(X, y_true, z_hidden, a_hidden, z_output, y_pred):
    error = y_pred - y_true
    d_z_output = error
    d_weights_hidden_output = np.dot(a_hidden.T, d_z_output)
    d_bias_output = np.sum(d_z_output, axis=0, keepdims=True)

    d_a_hidden = np.dot(d_z_output, weights_hidden_output.T)
    d_z_hidden = d_a_hidden * sigmoid_derivative(a_hidden)
    d_weights_input_hidden = np.dot(X.T, d_z_hidden)
    d_bias_hidden = np.sum(d_z_hidden, axis=0, keepdims=True)

    return d_weights_input_hidden, d_bias_hidden, d_weights_hidden_output, d_bias_output


# 训练过程
epochs = 10000
for epoch in range(epochs):
    z_hidden, a_hidden, z_output, y_pred = forward_propagation(X_train)
    d_weights_input_hidden, d_bias_hidden, d_weights_hidden_output, d_bias_output = backward_propagation(
        X_train, y_train, z_hidden, a_hidden, z_output, y_pred)

    # 更新权重和偏置
    weights_input_hidden -= learning_rate * d_weights_input_hidden
    bias_hidden -= learning_rate * d_bias_hidden
    weights_hidden_output -= learning_rate * d_weights_hidden_output
    bias_output -= learning_rate * d_bias_output

    if epoch % 1000 == 0:
        loss = np.mean(np.square(y_pred - y_train))
        print(f'Epoch {epoch}, Loss: {loss}')

# 测试
X_test = np.linspace(-10, 10, 100).reshape(-1, 1)
z_hidden, a_hidden, z_output, y_pred_test = forward_propagation(X_test)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(X_train, y_train, 'ro', label='Training Data')
plt.plot(X_test, y_pred_test, label='Predicted Function')
plt.xlabel('x')
plt.ylabel('|x|')
plt.title('Neural Network Simulation of y = |x|')
plt.legend()
plt.grid(True)
plt.show()






