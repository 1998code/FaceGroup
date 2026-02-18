import os
import shutil
import face_recognition
import cv2
import numpy as np
from pathlib import Path

# --- CONFIGURATION ---
INPUT_DIR = "input_images"
OUTPUT_DIR = "output_groups"
TOLERANCE = 0.5  # Lower is more strict (less false positives), higher is more loose. 0.5-0.6 is typical.
# For Asian faces, sometimes 0.45 - 0.5 works best to avoid mixing similar people.

def group_faces():
    # Create directories if they don't exist
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"Created '{INPUT_DIR}' folder. Please put your images there and run again.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Store known face encodings and their assigned ID
    known_face_encodings = []
    known_face_ids = []
    
    # Supported image extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    
    image_paths = [str(p) for p in Path(INPUT_DIR).glob("**/*") if p.suffix.lower() in valid_extensions]
    
    if not image_paths:
        print(f"No images found in {INPUT_DIR}.")
        return

    print(f"Found {len(image_paths)} images. Starting processing...")

    person_count = 0

    for img_path in image_paths:
        print(f"Processing: {os.path.basename(img_path)}...")
        
        try:
            # Load the image
            image = face_recognition.load_image_file(img_path)
            
            # Find all face locations and encodings in the image
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            if not face_encodings:
                # No faces found - move to an "unknown" or "no_face" folder if desired
                no_face_dir = os.path.join(OUTPUT_DIR, "no_faces_detected")
                os.makedirs(no_face_dir, exist_ok=True)
                shutil.copy(img_path, no_face_dir)
                continue

            # Process each face found in the image
            for i, face_encoding in enumerate(face_encodings):
                # See if the face is a match for any known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=TOLERANCE)
                
                person_id = None

                # Use the first match found, or finding the one with the smallest distance
                if True in matches:
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        person_id = known_face_ids[best_match_index]
                
                # If no match, it's a new person
                if person_id is None:
                    person_count += 1
                    person_id = f"Person_{person_count}"
                    known_face_encodings.append(face_encoding)
                    known_face_ids.append(person_id)
                    
                    # Create a folder for the new person
                    person_dir = os.path.join(OUTPUT_DIR, person_id)
                    os.makedirs(person_dir, exist_ok=True)
                    
                    # Optionally, save a thumbnail of the face to identify the folder
                    top, right, bottom, left = face_locations[i]
                    face_image = image[top:bottom, left:right]
                    # Convert from RGB (face_recognition) to BGR (cv2)
                    face_image = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
                    cv2.imwrite(os.path.join(person_dir, "representative_face.jpg"), face_image)

                # Copy image to the person's folder
                # Note: if the same person appears multiple times in one image, it only gets copied once
                # But if there are multiple DIFFERENT people, it gets copied to each of their folders
                target_path = os.path.join(OUTPUT_DIR, person_id, os.path.basename(img_path))
                if not os.path.exists(target_path):
                    shutil.copy(img_path, target_path)

        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    print("\nProcessing complete!")
    print(f"Groups created in '{OUTPUT_DIR}'")

if __name__ == "__main__":
    group_faces()
