import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 设置图像数据生成器
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

# 加载训练集数据
train_generator = datagen.flow_from_directory(
    'path/to/training_data',
    target_size=(64, 64),  # 设置图像大小
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

# 加载验证集数据
validation_generator = datagen.flow_from_directory(
    'path/to/training_data',
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)
model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))  # num_classes 为类别数量
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_generator, epochs=10, validation_data=validation_generator)
test_loss, test_acc = model.evaluate(test_generator)
print(f'Test accuracy: {test_acc}')

