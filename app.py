from flask import Flask, request, jsonify
from RekognitionImage import RekognitionImage
import boto3
import base64


app = Flask(__name__)
# Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials
aws_access_key = 'AKIAXUYDI7HIDJBV2VRZ'
aws_secret_key = 'F5Z1p87csUcvKSoJantSY9FdGgPLDEEoeYkveHro'
aws_region = 'us-east-1'
# Initialize the Rekognition client
rekognition_client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

@app.route("/analyze/faces", methods=["POST"])
def analyze_faces():
    # Get image data from request
    image_data = request.files["image"].read()
    # Encode the image data in base64 format
    encoded_image = base64.b64encode(image_data)
    Image={"Bytes": image_data}
    image_name = request.files["image"].filename

    # Create RekognitionImage instance and use detect_faces
    rekognition_image = RekognitionImage(Image, image_name,rekognition_client)
    faces = rekognition_image.detect_faces()
    return faces
    # Return detected faces as JSON
    # return jsonify({"faces": [face.to_dict() for face in faces]})


@app.route("/analyze/labels", methods=["POST"])
def analyze_labels():
    # Get image data from request and max labels
    image_data = request.files["image"].read()
    image_name = request.files["image"].filename
    max_labels = request.args.get("max_labels", 10, type=int)
    Image={"Bytes": image_data}
    # Create RekognitionImage instance and use detect_labels
    rekognition_image = RekognitionImage(Image, image_name,rekognition_client)
    labels = rekognition_image.detect_labels(max_labels)

    # Return detected labels as JSON
    return jsonify({"labels": [label.to_dict() for label in labels]})


@app.route("/analyze/moderation", methods=["POST"])
def analyze_moderation():
    # Get image data from request
    image_data = request.files["image"].read()
    image_name = request.files["image"].filename

    # Create RekognitionImage instance and use detect_moderation_labels
    rekognition_image = RekognitionImage(image_data, image_name)
    moderation_labels = rekognition_image.detect_moderation_labels()

    # Return moderation labels as JSON
    return jsonify({"moderation_labels": [label.to_dict() for label in moderation_labels]})


@app.route("/analyze/text", methods=["POST"])
def analyze_text():
    # Get image data from request
    image_data = request.files["image"].read()
    image_name = request.files["image"].filename

    # Create RekognitionImage instance and use detect_text
    rekognition_image = RekognitionImage(image_data, image_name)
    texts = rekognition_image.detect_text()

    # Return detected text as JSON
    return jsonify({"text": [text.to_dict() for text in texts]})


if __name__ == "__main__":
    app.run(debug=True)
