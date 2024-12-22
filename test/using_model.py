import tensorflow as tf
import numpy as np

def load_and_use_tflite(tflite_model_path):
    """
    Load a TensorFlow Lite model and use it for prediction
    
    Args:
        tflite_model_path (str): Path to the .tflite model file
    
    Returns:
        TFLite Interpreter
    """
    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
    interpreter.allocate_tensors()
    
    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # Function to predict using the TFLite model
    def predict(input_data):
        # Prepare input data
        input_data = np.array(input_data, dtype=np.float32).reshape(input_details[0]['shape'])
        
        # Set the tensor to point to the input data to be inferred
        interpreter.set_tensor(input_details[0]['index'], input_data)
        
        # Run inference
        interpreter.invoke()
        
        # Get the output tensor
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        return output_data
    
    return predict

tflite_model_path = 'linear_model.tflite'
# Load the TFLite model
tflite_predict = load_and_use_tflite(tflite_model_path)
# Make predictions
test_input = [10.0]
print("TFLite Model Prediction:", tflite_predict(test_input))