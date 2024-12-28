import streamlit as st
from streamlit_clickable_images import clickable_images
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

# Class names for Fashion MNIST
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def load_model():
    """Load the trained model"""
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
    
    return model

def convert_image_to_base64(image_array):
    """Convert numpy array to base64 string"""
    plt.figure(figsize=(3, 3))
    plt.imshow(image_array, cmap='gray')
    plt.axis('off')
    
    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    
    # Convert to base64
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/png;base64,{image_base64}"

def main():
    st.title("Fashion MNIST Classifier")
    st.write("Click on any image to see its prediction!")

    # Load the model
    model = load_model()

    # Load Fashion MNIST dataset
    (_, _), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
    
    # Select first 25 test images
    display_images = test_images[:25]
    display_labels = test_labels[:25]

    # Convert images to base64 strings
    image_paths = [convert_image_to_base64(img) for img in display_images]

    # Create columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # Display clickable image grid
        clicked = clickable_images(
            image_paths,
            titles=[f"Image {i+1}" for i in range(len(image_paths))],
            div_style={"display": "grid", "grid-template-columns": "repeat(5, 1fr)", "gap": "10px"},
            img_style={"cursor": "pointer", "border-radius": "5px", 
                      "transition": "transform 0.3s", "width": "100%"}
        )

    # Display prediction in the second column
    with col2:
        if clicked > -1:  # If an image was clicked
            st.write("### Selected Image")
            selected_image = display_images[clicked]
            st.image(selected_image, caption=f'Image {clicked + 1}', width=200)
            
            # Preprocess and predict
            processed_image = selected_image / 255.0
            prediction = model.predict(processed_image.reshape(1, 28, 28))
            predicted_class = np.argmax(prediction)
            actual_class = display_labels[clicked]
            
            st.write("### Prediction Results")
            st.write(f"Predicted: **{class_names[predicted_class]}**")
            st.write(f"Actual: **{class_names[actual_class]}**")
            
            # Show prediction probabilities
            st.write("### Confidence Scores")
            for i, prob in enumerate(prediction[0]):
                st.progress(float(prob))
                st.write(f"{class_names[i]}: {prob*100:.1f}%")

if __name__ == '__main__':
    main()