import os
import shutil
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI()

# Basic categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"]
}

unknown_folder = "Others"


# ---------------- AI FUNCTION ----------------
def classify_with_ai(file_name):
    """
    Uses AI to decide:
    - category
    - better filename
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a file organizer. Return ONLY: category,new_name"
            },
            {
                "role": "user",
                "content": f"Classify this file: {file_name}"
            }
        ]
    )

    result = response.choices[0].message.content.strip()

    try:
        category, new_name = result.split(",")
        return category.strip(), new_name.strip()
    except:
        return "Others", file_name


# ---------------- MAIN FUNCTION ----------------
def organize_folder(path):

    files = os.listdir(path)

    for file in files:

        full_path = os.path.join(path, file)

        if not os.path.isfile(full_path):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        moved = False

        # -------- BASIC TYPE HANDLING --------
        for folder, extensions in file_types.items():

            if extension in extensions:

                folder_path = os.path.join(path, folder)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                destination = os.path.join(folder_path, file)
                shutil.move(full_path, destination)

                print(f"[BASIC] {file} → {folder}/")
                moved = True
                break

        # -------- AI HANDLING --------
        if not moved:

            category, new_name = classify_with_ai(file)

            folder_path = os.path.join(path, category)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            destination = os.path.join(folder_path, new_name)

            shutil.move(full_path, destination)

            print(f"[AI] {file} → {category}/{new_name}")


# ---------------- RUN ----------------
if __name__ == "__main__":
    path = input("Enter folder path: ")
    organize_folder(path)