import tensorflow as tf
import numpy as np

def load_and_use_tflite(tflite_model_path):
    """
    載入雙變量 TensorFlow Lite 模型並進行預測
    
    Args:
        tflite_model_path (str): .tflite 模型檔案路徑
    
    Returns:
        function: 預測函數
    """
    try:
        # 載入 TFLite 模型
        interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
        interpreter.allocate_tensors()
        
        # 獲取輸入和輸出張量資訊
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        def predict(input_data):
            """
            使用模型進行預測
            
            Args:
                input_data (list): 包含兩個輸入值的列表 [x1, x2]
            
            Returns:
                np.array: 預測結果
            """
            if len(input_data) != 2:
                raise ValueError("需要exactly兩個輸入值")
                
            # 準備輸入數據
            input_array = np.array(input_data, dtype=np.float32).reshape(input_details[0]['shape'])
            
            # 設置輸入張量
            interpreter.set_tensor(input_details[0]['index'], input_array)
            
            # 執行推論
            interpreter.invoke()
            
            # 獲取輸出張量
            output_data = interpreter.get_tensor(output_details[0]['index'])
            
            return output_data
        
        return predict
        
    except Exception as e:
        print(f"模型載入錯誤: {str(e)}")
        return None

if __name__ == "__main__":
    # 載入模型
    model_path = 'linear_model_2var.tflite'
    predict_fn = load_and_use_tflite(model_path)
    
    if predict_fn is not None:
        # 測試案例
        test_inputs = [
            [1.0, 2.0],
            [2.0, 3.0],
            [3.0, 4.0]
        ]
        
        for test_input in test_inputs:
            try:
                result = predict_fn(test_input)
                print(f"輸入: {test_input}, 預測結果: {result[0][0]}")
            except Exception as e:
                print(f"預測錯誤: {str(e)}")