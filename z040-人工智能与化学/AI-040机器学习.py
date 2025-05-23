import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体或其他支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 加载数据集
iris = datasets.load_iris()
X = iris.data[:, :2]  # 选择前两个特征：萼片长度和宽度
y = iris.target  # 标签

# 数据集划分：70% 训练集，30% 测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据预处理：标准化特征值
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# 创建KNN分类器实例
k = 5  # 设置邻居数为5
knn = KNeighborsClassifier(n_neighbors=k)

# 训练模型
knn.fit(X_train, y_train)

# 预测测试集
y_pred = knn.predict(X_test)

# 评估模型
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))


# 自定义分类报告
def custom_classification_report(y_true, y_pred, target_names):
    from sklearn.metrics import precision_recall_fscore_support
    precision, recall, f1, support = precision_recall_fscore_support(y_true, y_pred, average=None)

    report = "分类报告:\n"
    header = f"{'':<15} {'精确率':<10} {'召回率':<10} {'F1分数':<10} {'支持度':<10}\n"
    report += header
    for i in range(len(target_names)):
        line = f"{target_names[i]:<15} {precision[i]:<10.2f} {recall[i]:<10.2f} {f1[i]:<10.2f} {support[i]:<10}\n"
        report += line
    return report


# 获取分类报告
target_names = ['山鸢尾', '变色鸢尾', '维吉尼亚鸢尾']
report = custom_classification_report(y_test, y_pred, target_names)
print(report)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率: {accuracy * 100:.2f}%")

# 可视化部分 - 选择前两个特征进行可视化
plt.figure(figsize=(8, 6))

# 绘制训练数据
for i, target_name in enumerate(target_names):
    plt.scatter(X_train[y_train == i, 0], X_train[y_train == i, 1], label=f"{target_name} (训练集)", marker='o')

# 绘制测试数据及其预测结果
for i, target_name in enumerate(target_names):
    plt.scatter(X_test[y_test == i, 0], X_test[y_test == i, 1], label=f"{target_name} (测试集真实)", marker='x')
    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1], label=f"{target_name} (测试集预测)", marker='s', edgecolors='black')

# 绘制决策边界
h = .02  # 网格步长
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = knn.predict(scaler.transform(np.c_[xx.ravel(), yy.ravel()]))
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)

plt.xlabel('特征1 (萼片长度)')
plt.ylabel('特征2 (萼片宽度)')
plt.title('Iris 数据可视化及 KNN 预测结果与决策边界')
plt.legend()
plt.show()