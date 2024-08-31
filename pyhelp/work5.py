import os

def get_all_files(directory, valid_extensions=None):
    """
    Get all files from the given directory (including subdirectories) with the specified extensions.
    If valid_extensions is None, all files are returned.
    """
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if valid_extensions:
                if file.lower().endswith(valid_extensions):
                    all_files.append(os.path.join(root, file))
            else:
                all_files.append(os.path.join(root, file))
    return all_files

def sync_labels_with_images(images_dir, labels_dir):
    """
    Ensure labels directory only keeps annotation files corresponding to images present in the images directory.
    """
    # Get all image files and corresponding label files
    image_files = get_all_files(images_dir, valid_extensions=('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
    label_files = get_all_files(labels_dir, valid_extensions=('.txt', '.xml'))  # Assuming annotations are in .txt or .xml

    # Create a set of image basenames (without extension)
    image_basenames = set(os.path.splitext(os.path.basename(image))[0] for image in image_files)

    # Iterate through label files and delete those that don't have a corresponding image
    for label_file in label_files:
        label_basename = os.path.splitext(os.path.basename(label_file))[0]
        if label_basename not in image_basenames:
            print(f"Deleting label file: {label_file}")
            os.remove(label_file)
        else:
            # Maintain the same directory structure in the labels directory
            relative_path = os.path.relpath(label_file, labels_dir)
            target_dir = os.path.join(labels_dir, os.path.dirname(relative_path))
            if not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)

if __name__ == "__main__":
    images_directory = 'Dataset-Annotate\images'
    labels_directory = 'Dataset-Annotate\labels'

    sync_labels_with_images(images_directory, labels_directory)
