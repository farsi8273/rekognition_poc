class RekognitionModerationLabel:
    def __init__(self, moderation_data):
        # Check if there are any moderation labels before initializing
        if not moderation_data["ModerationLabels"]:
            raise ValueError("No moderation labels found in response.")
        self.model_version = moderation_data["ModerationModelVersion"]
        self.response_metadata = moderation_data["ResponseMetadata"]
        # Empty since no labels are present
        self.labels = []

    def to_dict(self):
        data = {
            "model_version": self.model_version,
            "response_metadata": self.response_metadata,
            "labels": self.labels,
        }
        return data

    def __str__(self):
        if not self.labels:
            return f"No moderation labels detected."
        return f"Moderation Labels ({self.model_version}):\n" + "\n".join(str(label) for label in self.labels)

    def add_label(self, label_data):
        # Implement logic to parse and store individual labels (not shown here)
        # based on the format of the "label_data" dictionary
        # Update the "self.labels" list accordingly
        pass

    # Add other methods as needed, like filtering labels by confidence or type

