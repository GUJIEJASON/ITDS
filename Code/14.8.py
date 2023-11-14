import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.nn import GCNConv
from torch_geometric.data import DataLoader
from torch_geometric.datasets import Planetoid
from sklearn.metrics import accuracy_score

# 设置随机种子以确保实验的可重复性
torch.manual_seed(42)

# 加载Cora数据集
dataset = Planetoid(root='cora', name='Cora')

# 定义图卷积网络 (GCN) 模型
class GCN(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index

        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)

        return x

# 设置模型参数
in_channels = dataset.num_features
hidden_channels = 64
out_channels = dataset.num_classes

# 初始化模型
model = GCN(in_channels, hidden_channels, out_channels)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)

# 将数据集分为训练集、验证集和测试集
train_loader = DataLoader(dataset, batch_size=1, shuffle=True)

# 使用数据集中的训练掩码
train_mask = dataset[0].train_mask
val_mask = dataset[0].val_mask
test_mask = dataset[0].test_mask

# 训练模型
epochs = 200
for epoch in range(epochs):
    model.train()
    for data in train_loader:
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out[train_mask], data.y[train_mask])
        loss.backward()
        optimizer.step()

    # 验证模型
    model.eval()
    with torch.no_grad():
        val_loss = criterion(out[val_mask], data.y[val_mask])
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {val_loss.item()}')

# 在测试集上评估模型
model.eval()
with torch.no_grad():
    test_out = model(dataset[0])
    predictions = test_out.argmax(dim=1)
    accuracy = accuracy_score(dataset[0].y[test_mask], predictions[test_mask])
    print(f'Test Accuracy: {accuracy * 100:.2f}%')
