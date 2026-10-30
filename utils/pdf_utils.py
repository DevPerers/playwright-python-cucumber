import re
from pathlib import Path

from pypdf import PdfReader

DOWNLOADS_DIR = Path(__file__).resolve().parent.parent / "downloads"


def clear_downloads_folder(downloads_dir=DOWNLOADS_DIR) -> int:
    """Delete the files in the downloads folder (Cypress task `clearDownloadsFolder`)."""
    downloads_dir = Path(downloads_dir)
    if not downloads_dir.exists():
        return 0
    deleted = 0
    for entry in downloads_dir.iterdir():
        if entry.is_file():
            entry.unlink()
            deleted += 1
    return deleted


def save_download(download, downloads_dir=DOWNLOADS_DIR) -> Path:
    """Save a Playwright download into the downloads folder and return its path."""
    downloads_dir = Path(downloads_dir)
    downloads_dir.mkdir(parents=True, exist_ok=True)
    target = downloads_dir / download.suggested_filename
    download.save_as(target)
    return target


def read_pdf(path) -> str:
    """Return the text of a PDF file (Cypress task `readPdf`)."""
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def read_pdf_normalized(path) -> str:
    return re.sub(r"\s+", " ", read_pdf(path).strip())
