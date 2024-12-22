import tensorflow as tf
import numpy as np

# Convert the model to TensorFlow Lite
def convert_to_tflite(model, output_path='model.tflite'):
    """
    Convert a TensorFlow Keras model to TensorFlow Lite format
    
    Args:
        model (tf.keras.Model): The trained Keras model
        output_path (str): Path to save the converted TFLite model
    
    Returns:
        bytes: TFLite model in byte format
    """
    # Convert the model
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Optional: Add optimization techniques
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    
    # Convert the model
    tflite_model = converter.convert()
    
    # Save the model to disk
    with open(output_path, 'wb') as f:
        f.write(tflite_model)
    
    print(f"TFLite model saved to {output_path}")

# Original model training for 2-variable equation z = 2x + 3y - 1
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[2])
])
model.compile(optimizer='sgd', loss='mean_squared_error')

# Training data for z = 2x + 3y - 1
x = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
y = [2*(-1) + 3*(-1) - 1, 2*0 + 3*0 - 1, 2*1 + 3*1 - 1, 2*2 + 3*2 - 1, 2*3 + 3*3 - 1, 2*4 + 3*4 - 1]
xs = np.array(x, dtype=float)
ys = np.array(y, dtype=float)

model.fit(xs, ys, epochs=500)

# Convert the model to TFLite
tflite_model_path = 'linear_model_2var.tflite'
convert_to_tflite(model, tflite_model_path)

