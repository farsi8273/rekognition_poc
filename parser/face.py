class RekognitionFace:
    def __init__(self, face_data):
        self.bounding_box = face_data["BoundingBox"]
        self.confidence = face_data["Confidence"]
        self.age_range = face_data.get("AgeRange", None)
        self.beard = face_data.get("Beard", None)
        self.emotions = face_data.get("Emotions", [])
        self.eye_direction = face_data.get("EyeDirection", None)
        self.eyeglasses = face_data.get("Eyeglasses", None)
        self.eyes_open = face_data.get("EyesOpen", None)
        self.face_occluded = face_data.get("FaceOccluded", None)
        self.gender = face_data.get("Gender", None)
        self.landmarks = face_data.get("Landmarks", None)
        self.mouth_open = face_data.get("MouthOpen", None)
        self.mustache = face_data.get("Mustache", None)
        self.pose = face_data.get("Pose", None)
        self.quality = face_data.get("Quality", None)
        self.smile = face_data.get("Smile", None)
        self.sunglasses = face_data.get("Sunglasses", None)

    def to_dict(self):
        data = {
            "bounding_box": self.bounding_box,
            "confidence": self.confidence,
        }
        if self.age_range:
            data["age_range"] = self.age_range
        if self.beard:
            data["beard"] = self.beard
        data["emotions"] = [{"Type": emotion["Type"], "Confidence": emotion["Confidence"]} for emotion in self.emotions]
        if self.eye_direction:
            data["eye_direction"] = self.eye_direction
        if self.eyeglasses:
            data["eyeglasses"] = self.eyeglasses
        if self.eyes_open:
            data["eyes_open"] = self.eyes_open
        if self.face_occluded:
            data["face_occluded"] = self.face_occluded
        if self.gender:
            data["gender"] = self.gender
        if self.landmarks:
            data["landmarks"] = {landmark["Type"]: (landmark["X"], landmark["Y"]) for landmark in self.landmarks}
        if self.mouth_open:
            data["mouth_open"] = self.mouth_open
        if self.mustache:
            data["mustache"] = self.mustache
        if self.pose:
            data["pose"] = self.pose
        if self.quality:
            data["quality"] = self.quality
        if self.smile:
            data["smile"] = self.smile
        if self.sunglasses:
            data["sunglasses"] = self.sunglasses
        return data

    # Add other methods as needed, like analyzing emotions or predicting age based on specific information

