import os
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import webbrowser
import yt_dlp  # Import the yt-dlp library

# Global variable to store the last downloaded video path
last_downloaded_video = ""

# Function to download the video
def download_video():
    global last_downloaded_video
    url = url_entry.get()
    if url:
        output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # yt-dlp options
        ydl_opts = {
            'format': 'bestvideo[height<=1080][ext=mp4]',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'noprogress': True,  # Disable console progress
            'quiet': True,       # Run yt-dlp in quiet mode
        }

        # Clear the output area
        output_area.delete(1.0, tk.END)
        
        def run_download():
            global last_downloaded_video
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=True)
                    last_downloaded_video = ydl.prepare_filename(info_dict)
                
                messagebox.showinfo("Veiksmīgi", "Lejupielāde pabeigta!")
            except Exception as e:
                messagebox.showerror("Kļūda", f"Lejupielāde neizdevās! {str(e)}")

        threading.Thread(target=run_download).start()

# Function to open the Downloads folder and highlight the downloaded video
def open_downloads_folder():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    if last_downloaded_video and os.path.exists(last_downloaded_video):
        # Open the folder and select the video
        subprocess.run(f'explorer /select,"{last_downloaded_video}"')
    else:
        webbrowser.open(downloads_folder)

# Create the GUI window
root = tk.Tk()
root.title("YouTube Video Lejuplādes Rīks")

# URL entry
url_label = tk.Label(root, text="Ievadiet YouTube video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Download button
download_button = tk.Button(root, text="Lejupielādēt video", command=download_video)
download_button.pack(pady=10)

# Open folder button
open_folder_button = tk.Button(root, text="Atvērt lejuplāžu mapi", command=open_downloads_folder)
open_folder_button.pack(pady=10)

# Output area
output_area = scrolledtext.ScrolledText(root, width=60, height=20)
output_area.pack(pady=10)

# Start the GUI loop
root.mainloop()
