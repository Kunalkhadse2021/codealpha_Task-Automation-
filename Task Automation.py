
import os
import shutil


def sanitize_path(path):
    """Normalize a user-entered path and remove common wrapping quotes."""
    if path is None:
        return ""
    cleaned = path.strip().strip('"').strip("'")
    return os.path.abspath(os.path.normpath(cleaned))


def organize_jpg_files():
    print("=" * 45)
    print("       JPG FILE ORGANIZER")
    print("=" * 45)

    student_name = input("Enter student name: ").strip()
    student_name = student_name or "Student"

    source_folder = sanitize_path(input("Enter the source folder path: "))

    if not os.path.isdir(source_folder):
        print("Error: Source folder does not exist.")
        return

    destination_folder = os.path.join(source_folder, "Organized_Images")
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if not os.path.isfile(source_path):
            continue

        if not filename.lower().endswith((".jpg", ".jpeg")):
            continue

        destination_path = os.path.join(destination_folder, filename)

        if os.path.exists(destination_path):
            print(f"Skipped duplicate filename: {filename}")
            continue

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1
        except OSError as error:
            print(f"Could not move {filename}: {error}")

    print("\n" + "=" * 45)
    print("AUTOMATION COMPLETED")
    print("Student Name:", student_name)
    print("Images moved:", moved_count)
    print("Destination:", destination_folder)
    print("=" * 45)


if __name__ == "__main__":
    organize_jpg_files()
