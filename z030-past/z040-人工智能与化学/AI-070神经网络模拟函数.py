import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# 生成训练数据
num_samples = 1000
X_train = np.random.uniform(-10, 10, num_samples).reshape(-1, 1)
y_train = np.abs(X_train)

# 构建神经网络模型
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(32, activation='relu'),
    Dense(1)
])

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
history = model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

# 测试模型
X_test = np.linspace(-10, 10, 100).reshape(-1, 1)
y_pred = model.predict(X_test)

# 绘制结果
plt.figure(figsize=(10, 5))
plt.plot(X_test, y_pred, label='Predicted')
plt.plot(X_test, np.abs(X_test), label='True', linestyle='--')
plt.xlabel('Input X')
plt.ylabel('Output Y')
plt.title('Neural Network Simulation of Absolute Value Function')
plt.legend()
plt.show()