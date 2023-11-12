import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image

# 定义神经网络模型
class GrayscaleResizer(nn.Module):
    def __init__(self, target_size):
        super(GrayscaleResizer, self).__init__()
        self.target_size = target_size

    def forward(self, x):
        # 将彩色图片转化为灰度图像
        grayscale_image = x.mean(dim=1, keepdim=True)

        # 调整图片大小
        resized_image = F.interpolate(grayscale_image, size=self.target_size, mode='bilinear', align_corners=False)

        return resized_image

if __name__ == '__main__':
    input_image_path = 'D:\VS Code\ITDS\Week7\\1.jpg'  # 请替换为您的图片文件路径
    output_image_path = 'D:\VS Code\ITDS\Week7\\2.jpg'  # 输出的处理后图片文件路径
    target_size = (100, 100)  # 目标宽度和高度

    # 打开图片并应用转换
    image = Image.open(input_image_path)
    transform = transforms.Compose([transforms.ToTensor()])
    image_tensor = transform(image).unsqueeze(0)

    # 初始化模型
    model = GrayscaleResizer(target_size)

    # 执行模型
    resized_image = model(image_tensor)

    # 保存处理后的图片
    output_image = transforms.ToPILImage()(resized_image.squeeze(0))
    output_image.save(output_image_path)

    print(f'处理后的图片已保存到 {output_image_path}')
