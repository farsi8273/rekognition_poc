class RekognitionLabel:
    def __init__(self, label_data):
        self.name = label_data["Name"]
        self.confidence = label_data["Confidence"]
        self.categories = [category["Name"] for category in label_data["Categories"]]
        self.aliases = [alias["Name"] for alias in label_data["Aliases"]]
        self.parents = [parent["Name"] for parent in label_data["Parents"]]
        self.instances = label_data.get("Instances", [])  # Optional for some labels

    def to_dict(self):
        data = {
            "name": self.name,
            "confidence": self.confidence,
            "categories": self.categories,
            "aliases": self.aliases,
            "parents": self.parents,
        }
        if self.instances:
            data["instances"] = [
                {
                    "bounding_box": instance["BoundingBox"],
                    "confidence": instance["Confidence"],
                }
                for instance in self.instances
            ]
        return data

    def __str__(self):
        return f"Label: {self.name} (Confidence: {self.confidence})"

    # Add additional methods as needed, like filtering by categories or parents
