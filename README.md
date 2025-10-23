CS50P File Organizer
A Python command-line tool to organize files in any folder by type—images, documents, audio, video, and more.

# How to Use
1.Clone this repo or download the files.

2.Install pytest (for running tests):
    pip install pytest

3.Run the organizer:
    python project.py
-When prompted, enter the folder path (e.g., ./testfolder). Leave blank for current directory.

4.Your files will be sorted into subfolders by type: Images, Docs, Audio, Video, Others.

# How to Run Unit Tests
From the project directory, run:
    pytest test_project.py
-Features
    Automatically sorts files in a folder by their extension/type.
    Avoids overwriting files with the same name (adds suffix).
    Supports common formats: jpg, png, mp3, mp4, pdf, docx, etc.
    Ignores subfolders (MVP); does not require extra packages.
    Includes full test suite for core functions.

-Example
    If your folder has:

    text
    photo.jpg
    resume.pdf
    song.mp3
    video.mp4
    unknown.xyz

    After running, it will have:

    text
    Images/photo.jpg
    Docs/resume.pdf
    Audio/song.mp3
    Video/video.mp4
    Others/unknown.xyz

# Project Details
-All code is in project.py
-Tests in test_project.py
-No dependencies beyond Python >= 3.6 (except optional pytest for tests)
-Developed by [Abhay Pratap Singh]

## Demo Video
See attached video file or link for demonstration of usage.

# License
For CS50P course project use only.