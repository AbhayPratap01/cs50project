import os
import shutil
import project

def test_get_category():
    assert project.get_category("nature.jpg") == "Images"
    assert project.get_category("resume.pdf") == "Docs"
    assert project.get_category("track.mp3") == "Audio"
    assert project.get_category("movie.mp4") == "Video"
    assert project.get_category("archive.zip") == "Others"

def test_move_file(tmp_path):
    source = tmp_path / "a.txt"
    source.write_text("sample")
    dest_dir = tmp_path / "dest"
    project.move_file(str(source), str(dest_dir))
    assert os.path.exists(os.path.join(dest_dir, "a.txt"))

def test_organize_folder(tmp_path):
    (tmp_path / "x.jpg").write_text("img")
    (tmp_path / "y.txt").write_text("doc")
    (tmp_path / "z.zip").write_text("other")
    count = project.organize_folder(str(tmp_path))
    assert count == 3
    assert os.path.exists(tmp_path / "Images" / "x.jpg")
    assert os.path.exists(tmp_path / "Docs" / "y.txt")
    assert os.path.exists(tmp_path / "Others" / "z.zip")
