import os
import random
import shutil

def select_images_by_prefix(directory, sample_size):
    # Create a dictionary to hold lists of image filenames, keyed by their prefix
    images_by_prefix = {}
    
    # List all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Get the first character of the filename as the prefix
            prefix = filename[0].lower()
            if prefix not in images_by_prefix:
                images_by_prefix[prefix] = []
            images_by_prefix[prefix].append(filename)
    
    # Calculate the number of images to sample per prefix
    total_prefixes = len(images_by_prefix)
    images_per_prefix = sample_size // total_prefixes
    
    # If the sample size is not evenly divisible by the number of prefixes,
    # calculate the remaining images to sample randomly from any prefix
    remaining_images = sample_size % total_prefixes
    
    selected_images = []
    
    for prefix, images in images_by_prefix.items():
        # Randomly sample the calculated number of images for each prefix
        selected_images.extend(random.sample(images, min(images_per_prefix, len(images))))
    
    # Randomly sample the remaining images if necessary
    if remaining_images > 0:
        all_images = [img for imgs in images_by_prefix.values() for img in imgs]
        additional_images = random.sample(all_images, remaining_images)
        selected_images.extend(additional_images)
    
    return selected_images

def main():
    # Define the directory containing the images and the required sample size
    image_directory = 'Dataset-Cleaning/pistol'
    sample_size = 600  # Replace with your desired sample size

    # Get the selected images
    selected_images = select_images_by_prefix(image_directory, sample_size)

    # Print or process the selected images
    print(f"Selected {len(selected_images)} images:")
    for image in selected_images:
        print(image)

    # Optionally, copy the selected images to a new directory
    selected_images_directory = 'Dd/pistol'
    os.makedirs(selected_images_directory, exist_ok=True)
    for image in selected_images:
        shutil.copy(os.path.join(image_directory, image), os.path.join(selected_images_directory, image))

if __name__ == "__main__":
    main()
