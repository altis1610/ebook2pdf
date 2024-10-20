from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import os
from PIL import Image
import shutil
import tkinter as tk
from tkinter import simpledialog, messagebox
import img2pdf
from PyPDF2 import PdfMerger
import glob

def setup_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def switch_to_new_window(driver, original_window):
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

def setup_folders(current_dir, project_name):
    project_folder = os.path.join(current_dir, project_name)
    screenshot_folder = os.path.join(project_folder, "book")
    pagefolder = os.path.join(screenshot_folder, "page")
    for folder in [project_folder, screenshot_folder, pagefolder]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
    return project_folder, screenshot_folder, pagefolder

def save_cover(driver, pagefolder, cut_l, cut_r):
    screenshot_path = os.path.join(pagefolder, "page_0.png")
    driver.save_screenshot(screenshot_path)
    print(f"Cover screenshot saved: {screenshot_path}")
    cover_image = Image.open(screenshot_path)
    width, height = cover_image.size
    cropped_cover = cover_image.crop((cut_l, 0, width - cut_r, height))
    width, height = cropped_cover.size
    cropped_cover = cropped_cover.crop((width // 2, 0, width, height))
    cropped_cover.save(screenshot_path)

def capture_pages(driver, total_runs, screenshot_folder, pagefolder, cut_l, cut_r):
    screenshot_count = 1
    page_count = 1
    run_count = 0
    while run_count < total_runs:
        window_size = driver.get_window_size()
        pyautogui.click(window_size['width'] - 10, window_size['height'] // 2)
        time.sleep(2.5)

        screenshot_path = os.path.join(screenshot_folder, f"screenshot_{screenshot_count}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

        image = Image.open(screenshot_path)
        width, height = image.size
        cropped_image = image.crop((cut_l, 0, width - cut_r, height))
        cropped_image.save(screenshot_path)

        width, height = cropped_image.size
        left_half = cropped_image.crop((0, 0, width // 2, height))
        right_half = cropped_image.crop((width // 2, 0, width, height))

        left_path = os.path.join(pagefolder, f"page_{page_count}.png")
        right_path = os.path.join(pagefolder, f"page_{page_count + 1}.png")

        left_half.save(left_path)
        right_half.save(right_path)

        page_count += 2
        screenshot_count += 1
        run_count += 1

        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(0.3)

def create_pdf(pagefolder, current_dir, project_name):
    page_files = sorted(glob.glob(os.path.join(pagefolder, "page_*.png")), 
                        key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))

    pdf_files = []
    for page_file in page_files:
        pdf_path = page_file.replace('.png', '.pdf')
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(page_file))
        pdf_files.append(pdf_path)

    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    output_path = os.path.join(current_dir, f"{project_name}.pdf")
    merger.write(output_path)
    merger.close()

    for pdf_file in pdf_files:
        os.remove(pdf_file)

    print(f"PDF created: {output_path}")
    return output_path

def cleanup(project_folder):
    shutil.rmtree(project_folder)
    print(f"Temporary folder removed: {project_folder}")

def main():
    root = tk.Tk()
    root.withdraw()

    project_name = simpledialog.askstring("專案名稱", "請輸入專案名稱")
    if project_name is None:
        print("程序已取消")
        return

    url = simpledialog.askstring("輸入網址", "請輸入登入網址網址", initialvalue="https://tpml.ebook.hyread.com.tw/")
    if url is None:
        print("程序已取消")
        return

    driver = setup_driver(url)
    original_window = driver.current_window_handle
    messagebox.showwarning("注意", "請跳轉到對應電子書頁面後再繼續操作")

    total_runs = simpledialog.askinteger("輸入頁數", "輸入頁數", initialvalue=5)
    if total_runs is None:
        print("程序已取消")
        driver.quit()
        return

    total_runs = (total_runs + 1) // 2

    switch_to_new_window(driver, original_window)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_folder, screenshot_folder, pagefolder = setup_folders(current_dir, project_name)

    cut_l, cut_r = 240, 240

    save_cover(driver, pagefolder, cut_l, cut_r)
    capture_pages(driver, total_runs, screenshot_folder, pagefolder, cut_l, cut_r)

    driver.quit()

    output_path = create_pdf(pagefolder, current_dir, project_name)
    cleanup(project_folder)

if __name__ == "__main__":
    main()