# Automated eBook Note Capture & PDF Archiver

This tool helps users **preserve their personal notes and reading highlights** from eBook platforms by automatically capturing key reading pages and compiling them into a clean, organized PDF for offline reference.

## ✨ Purpose

Many eBook platforms don’t allow long-term storage of your annotations or notes.  
This project provides a personal **note-keeping automation** — ideal for educational or research use — to retain the pages where you’ve made important highlights or comments.

> ⚠️ **Disclaimer:**  
> This tool is designed **only for personal educational use**. It should be used to preserve your **own reading notes or highlights**, not to duplicate or redistribute copyrighted eBooks.

---

## 🧭 Features

- Automatically opens Chrome and navigates to your eBook or note-taking page  
- Supports login and manual note access  
- Captures screenshots of **noted or highlighted pages**  
- Crops out browser borders for clean pages  
- Merges captured images into a single **PDF archive of your reading notes**  
- Custom project name and note-page count supported

---

## ⚙️ System Requirements

- Python 3.7 or newer  
- Google Chrome installed  
- ChromeDriver (auto-downloaded by the script)

---
## Installation Steps

### 1. Clone or Download the Project
```bash
git clone https://github.com/altis1610/ebook2pdf.git
cd Book_script
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Script
```bash
python book_v_1.py
```

### 2. Follow the Prompts

1. **Enter project name**: Name your output PDF
2. **Enter login URL**: Default is Taipei Public Library eBook platform
3. **Log in and navigate**: Use the browser to log in and open the desired eBook
4. **Confirm readiness**: Click "OK" in the popup dialog to start screenshot automation
5. **Enter page count**: Specify the number of pages to capture

### 3. Automated Process

The script will:
- Capture the cover page
- Take screenshots page by page and turn pages automatically
- Crop and split double-page images
- Generate the final PDF file

### 4. Output

After completion, the PDF will be saved in the same directory with the name you provided.

## Notes

1. **Chrome**: Ensure Google Chrome is installed
2. **Internet**: A stable internet connection is required
3. **Permissions**: On macOS, screen recording permission may be needed
4. **Don't touch the mouse**: Avoid using the mouse or interacting during capture
5. **Browser window**: Keep the Chrome window maximized and in the foreground

## Troubleshooting

### Chrome Not Found
```bash
# Ensure Chrome is installed or install ChromeDriver
brew install chromedriver  # macOS with Homebrew
```

### Dependency Installation Failed
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Screenshot Quality Issues
- Ensure the browser window is maximized
- Check network stability
- Adjust `cut_l` and `cut_r` parameters in the code for better cropping

## Exit the Virtual Environment

After you're done:
```bash
deactivate
```

## Supported Platforms

- macOS
- Windows
- Linux
