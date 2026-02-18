import os
import shutil
import face_recognition
import cv2
import numpy as np
import gradio as gr
from pathlib import Path
import time

# --- CONFIGURATION ---
INPUT_DIR = "input_images"
OUTPUT_DIR = "output_groups"

def process_faces(input_path, output_path, tolerance, progress=gr.Progress()):
    if not os.path.exists(input_path):
        return f"Input directory '{input_path}' not found.", []

    if os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    else:
        os.makedirs(output_path)

    known_face_encodings = []
    known_face_ids = []
    
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    image_paths = [str(p) for p in Path(input_path).glob("**/*") if p.suffix.lower() in valid_extensions]
    
    if not image_paths:
        return f"No images found in {input_path}.", []

    results_gallery = []
    person_count = 0
    
    progress(0, desc="Starting face recognition...")
    
    for idx, img_path in enumerate(image_paths):
        progress((idx + 1) / len(image_paths), desc=f"Processing {os.path.basename(img_path)}")
        
        try:
            image = face_recognition.load_image_file(img_path)
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            if not face_encodings:
                no_face_dir = os.path.join(output_path, "no_faces_detected")
                os.makedirs(no_face_dir, exist_ok=True)
                shutil.copy(img_path, no_face_dir)
                continue

            for i, face_encoding in enumerate(face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
                person_id = None

                if True in matches:
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        person_id = known_face_ids[best_match_index]
                
                if person_id is None:
                    person_count += 1
                    person_id = f"Person_{person_count}"
                    known_face_encodings.append(face_encoding)
                    known_face_ids.append(person_id)
                    
                    person_dir = os.path.join(output_path, person_id)
                    os.makedirs(person_dir, exist_ok=True)
                    
                    top, right, bottom, left = face_locations[i]
                    face_image = image[top:bottom, left:right]
                    face_image = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
                    rep_path = os.path.join(person_dir, "representative_face.jpg")
                    cv2.imwrite(rep_path, face_image)
                    results_gallery.append((rep_path, f"Person {person_count}"))

                target_path = os.path.join(output_path, person_id, os.path.basename(img_path))
                if not os.path.exists(target_path):
                    shutil.copy(img_path, target_path)

        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    return f"Processing complete! Found {person_count} unique people. Results saved to '{output_path}'", results_gallery

# Custom CSS for modern look
custom_css = """
.container { 
    max-width: 1000px; 
    margin: auto; 
    padding-top: 2rem;
}
.header {
    text-align: center;
    margin-bottom: 2rem;
}
.gr-button-primary {
    background: linear-gradient(90deg, #4f46e5, #7c3aed) !important;
    border: none !important;
    font-weight: bold !important;
}
.footer {
    text-align: center;
    margin-top: 2rem;
    color: #6b7280;
}
"""

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Column(elem_classes="container"):
        gr.Markdown(
            """
            # 🎨 Face Grouping Tool
            ### Organize your image library by recognizing and clustering faces automatically.
            """,
            elem_classes="header"
        )
        
        with gr.Row():
            with gr.Column(scale=2):
                input_folder = gr.Textbox(
                    label="📂 Input Folder Path", 
                    value="input_images",
                    placeholder="/path/to/your/photos"
                )
                output_folder = gr.Textbox(
                    label="📁 Output Folder Path", 
                    value="output_groups",
                    placeholder="/path/to/save/results"
                )
            
            with gr.Column(scale=1):
                tolerance = gr.Slider(
                    minimum=0.1, 
                    maximum=0.8, 
                    value=0.5, 
                    step=0.05, 
                    label="Strictness (Tolerance)", 
                    info="Lower is more strict. (Default: 0.5)"
                )
                start_btn = gr.Button("🚀 Start Grouping", variant="primary")
        
        status_output = gr.Textbox(label="Status", placeholder="Ready to process...")
        
        gr.Markdown("### 👤 Unique People Detected")
        gallery = gr.Gallery(
            label="Groups", 
            show_label=False, 
            columns=6, 
            rows=2, 
            height="auto",
            object_fit="contain"
        )
        
        gr.Markdown(
            "Instructions: Enter the paths to your input and output folders above and click 'Start Grouping'.",
            elem_classes="footer"
        )

    start_btn.click(
        fn=process_faces,
        inputs=[input_folder, output_folder, tolerance],
        outputs=[status_output, gallery]
    )

if __name__ == "__main__":
    demo.launch(css=custom_css)
