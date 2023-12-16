class RekognitionFace:
    def __init__(self, face_data):
        self.bounding_box = face_data["BoundingBox"]
        self.confidence = face_data["Confidence"]
        self.landmarks = face_data.get("Landmarks", None)  # Optional based on response
        self.pose = face_data.get("Pose", None)  # Optional based on response
        self.quality = face_data.get("Quality", None)  # Optional based on response

    def to_dict(self):
        data = {
            "bounding_box": self.bounding_box,
            "confidence": self.confidence,
        }
        if self.landmarks:
            data["landmarks"] = {
                landmark_type: point["X", "Y"]
                for landmark_type, point in self.landmarks.items()
            }
        if self.pose:
            data["pose"] = self.pose
        if self.quality:
            data["quality"] = self.quality
        return data

    def is_smiling(self):
        """
        Checks if the face is smiling based on landmarks (optional).
        """
        if self.landmarks:
            mouth_left = self.landmarks["MouthLeft"]
            mouth_right = self.landmarks["MouthRight"]
            distance = abs(mouth_left["Y"] - mouth_right["Y"])
            return distance > 0.4  # Threshold for smile detection
        else:
            return False

    # Add other methods as needed, like age estimation or emotion detection

