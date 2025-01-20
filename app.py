from flask import Flask, request, jsonify, render_template,send_from_directory
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

import os

# Initialize Flask app
app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model
model = load_model('E:\Project\wild life conservation\models\cnn_model.h5')

animal_data = pd.read_csv('E:\Project\wild life conservation\meta data\Animal.csv')
effecting_factors = pd.read_csv('E:\Project\wild life conservation\meta data\Effecting_Factor.csv')
endangered_data = pd.read_csv('E:\Project\wild life conservation\meta data\Endangered_Species.csv')
population_data = pd.read_csv('E:\Project\wild life conservation\meta data\Population_by_year.csv')
remedial_measures = pd.read_csv('E:\Project\wild life conservation\meta data\Remediation_measures.csv')

# Define animal class labels (adjust based on your model)
class_labels = ['Elephant(African)', 'Amur_Leopard', 'Arctic Fox', 'Chimpanzee', 
                'Jaguars', 'Lion', 'Orangutan', 'Panda', 'Panther', 'Rhino(Black)', 'Cheetahs']

# Helper function for image prediction
def predict_image(image_path):
    # Load and preprocess the image
    image = load_img(image_path, target_size=(180, 180))  # Match model input size
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    
    # Predict the class
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100
    return predicted_class_label, confidence

# Flask route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route for uploading and predicting an image
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Predict the class of the image
    predicted_class, confidence = predict_image(image_path)

    # Fetch additional data from the CSVs
    animal_info = animal_data[animal_data['Animal_Name'] == predicted_class].iloc[0]
    threats = effecting_factors[effecting_factors['Animal_Name'] == predicted_class].iloc[0]
    conservation = remedial_measures[remedial_measures['Animal_Name'] == predicted_class].iloc[0]

    # Prepare the population trend data
    population_trend = population_data[population_data['Animal'] == predicted_class]


    # Convert non-numeric values in 'Population' to NaN
    population_trend['Population'] = pd.to_numeric(population_trend['Population'], errors='coerce')

    # Group by 'Year' and sum 'Population', ignoring NaN values
    population_trend_grouped = population_trend.groupby('Year', as_index=False)['Population'].sum()
    

    # Check if there is valid population trend data
    show_population_trend = not population_trend_grouped.empty

    if show_population_trend:
        population_years = population_trend_grouped['Year'].tolist()
        population_values = population_trend_grouped['Population'].tolist()

        # Zip the years and population values together in Python
        zipped_population_data = list(zip(population_years, population_values))

        plt.figure(figsize=(14, 10))
        plt.plot(population_years, population_values, marker='o', linestyle='-', color='b', label='Population')
        plt.title(f'Population Trend for {predicted_class}',fontsize=18)
        plt.xlabel('Year',fontsize=16)
        plt.ylabel('Population',fontsize=16)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Save the plot to a BytesIO object
        img = BytesIO()
        plt.savefig(img, format='png',bbox_inches='tight')
        img.seek(0)
    
        # Encode the image to base64
        img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    else:
        population_years = []
        population_values = []
        zipped_population_data = list(zip(population_years, population_values))
        img_base64 = None
    
    if zipped_population_data:  # Ensure population_data exists and is not empty
       show_population_trend = True
    else:
       show_population_trend = False

    print(zipped_population_data)


    # Prepare the data for display
    details = {
        'Animal Name': animal_info['Animal_Name'],
        'Class': animal_info['Class'],
        'Population': animal_info['Population'],
        'Weight': animal_info['Weight'],
        'Length': animal_info['Length'],
        'Height': animal_info['Height'],
        'Habitats': animal_info['Habitats'],
        'Status': animal_info['Status'],
        'Country': animal_info['Country'],
        'Places': animal_info['Places'],
        'Threats': threats['Factor'],
        'Measures Taken': conservation['Measure_Taken'],
    }

    

    # Render the template with the data
    return render_template('result.html', 
                           image_url=f"/static/uploads/{image.filename}", 
                           details=details, 
                           confidence=f"{confidence:.2f}%",
                           img_base64=img_base64,
                           show_population_trend=show_population_trend,
                           population_data=zipped_population_data)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
