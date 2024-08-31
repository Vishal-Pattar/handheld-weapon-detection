import os
import json

def convert_class(class_id):
    class_map = {
        0: "pistol",
        2: "knife"
    }
    return class_map.get(class_id, "other")

def convert_annotation_to_json(annotation_str):
    values = annotation_str.strip().split()
    class_id = int(values[0])
    class_name = convert_class(class_id)
    annotation = {
        "class": class_name,
        "x1": float(values[1]),
        "y1": float(values[2]),
        "x2": float(values[3]),
        "y2": float(values[4])
    }
    return annotation, class_name

def convert_directory_to_json(directory_path):
    all_classes = set()
    
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            
            with open(file_path, "r") as file:
                annotation_str = file.read()
            
            annotation, class_name = convert_annotation_to_json(annotation_str)
            all_classes.add(class_name)
            
            json_filename = filename.replace(".txt", ".json")
            json_file_path = os.path.join(directory_path, json_filename)
            
            with open(json_file_path, "w") as json_file:
                json.dump(annotation, json_file, indent=4)
    
    print(f"Unique classes found in the annotation files: {sorted(all_classes)}")

directory_path = "./data/annotation/train"
convert_directory_to_json(directory_path)
