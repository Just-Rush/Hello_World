import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体或其他支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 加载数据集
iris = datasets.load_iris()
X = iris.data  # 选择所有特征
y = iris.target  # 标签

# 数据集划分：70% 训练集，30% 测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据预处理：标准化特征值
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# 使用 PCA 进行特征降维
pca = PCA(n_components=2)  # 保留两个主成分
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 创建 KNN 分类器实例
k = 5  # 设置邻居数为5
knn = KNeighborsClassifier(n_neighbors=k)

# 训练模型
knn.fit(X_train_pca, y_train)

# 预测测试集
y_pred = knn.predict(X_test_pca)

# 评估模型
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))
print("\n分类报告:")
print(classification_report(y_test, y_pred))
print(f"准确率: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# 可视化部分 - 选择前两个特征进行可视化
plt.figure(figsize=(8, 6))

# 绘制训练数据
for i, target_name in enumerate(iris.target_names):
    plt.scatter(X_train_pca[y_train == i, 0], X_train_pca[y_train == i, 1], label=f"{target_name} (训练集)", marker='o')

# 绘制测试数据及其预测结果
for i, target_name in enumerate(iris.target_names):
    plt.scatter(X_test_pca[y_test == i, 0], X_test_pca[y_test == i, 1], label=f"{target_name} (测试集真实)", marker='x')
    plt.scatter(X_test_pca[y_pred == i, 0], X_test_pca[y_pred == i, 1], label=f"{target_name} (测试集预测)", marker='s', edgecolors='black')

plt.xlabel('主成分1')
plt.ylabel('主成分2')
plt.title('PCA 处理后的 Iris 数据可视化及 KNN 预测结果')
plt.legend()
plt.show()