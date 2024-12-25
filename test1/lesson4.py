import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

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

def create_image_grid(images, labels, selected_idx=None):
    """Create a 5x5 grid of images with selection highlight"""
    fig, axs = plt.subplots(5, 5, figsize=(10, 10))
    fig.subplots_adjust(hspace=0.5)
    
    for idx, ax in enumerate(axs.flat):
        if idx < len(images):
            ax.imshow(images[idx], cmap='gray')
            if selected_idx == idx:
                # Highlight selected image with a red border
                ax.patch.set_edgecolor('red')
                ax.patch.set_linewidth(2)
            ax.axis('off')
            ax.set_title(f'Image {idx + 1}')
    
    return fig

def main():
    st.title("Fashion MNIST Classifier")
    st.write("Select an image from the grid to see its prediction!")

    # Load the model
    model = load_model()

    # Load Fashion MNIST dataset
    (_, _), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
    
    # Select first 25 test images
    display_images = test_images[:25]
    display_labels = test_labels[:25]

    # Create columns for layout
    col1, col2 = st.columns([2, 1])

    # Store the selected index in session state
    if 'selected_idx' not in st.session_state:
        st.session_state.selected_idx = None

    # Display image grid in the first column
    with col1:
        fig = create_image_grid(display_images, display_labels, st.session_state.selected_idx)
        st.pyplot(fig)
        
        # Create a 5x5 grid of buttons
        cols = st.columns(5)
        for i in range(25):
            col_idx = i % 5
            with cols[col_idx]:
                if st.button(f'Select {i + 1}', key=f'btn_{i}'):
                    st.session_state.selected_idx = i

    # Display prediction in the second column
    with col2:
        if st.session_state.selected_idx is not None:
            st.write("### Selected Image")
            selected_image = display_images[st.session_state.selected_idx]
            st.image(selected_image, caption=f'Image {st.session_state.selected_idx + 1}', width=200)
            
            # Preprocess and predict
            processed_image = selected_image / 255.0
            prediction = model.predict(processed_image.reshape(1, 28, 28))
            predicted_class = np.argmax(prediction)
            actual_class = display_labels[st.session_state.selected_idx]
            
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