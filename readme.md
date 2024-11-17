
---

# YouTube Video Lejuplādes Rīks (YouTube Video Downloader Tool)

This is a simple graphical user interface (GUI) tool built using Python's `tkinter` library and the `yt-dlp` library for downloading YouTube videos. The tool allows users to input a YouTube video URL and download the video directly to the "Downloads" folder.

---

## Features

- **Video Downloading**: Allows users to download YouTube videos in the best available quality up to 1080p, in MP4 format.
- **Multi-threaded**: The download process runs in a separate thread to prevent the GUI from freezing.
- **Folder Access**: After downloading, users can open their "Downloads" folder and directly access the downloaded video.
- **Error Handling**: Displays error messages in case of failure.

---

## Requirements

- **Python 3.x**  
- **Libraries**:  
  - `yt-dlp` (for downloading YouTube videos)
  - `tkinter` (for the GUI)

You can install the necessary libraries by running the following command:

```bash
pip install yt-dlp
```

**Note**: `tkinter` is typically included with Python, so no additional installation is usually required.

---

## Installation

1. Clone or download the repository to your local machine.
2. Install the necessary Python libraries using the following command:

   ```bash
   pip install yt-dlp
   ```

3. Run the Python script (`youtube_video_downloader.py`).

---

## Usage

1. Launch the program by running the Python script.
   
   ```bash
   python youtube_video_downloader.py
   ```

2. In the opened window, input a YouTube video URL in the text field.

3. Press the **Lejupielādēt video** (Download Video) button to start the download.

4. Once the download is complete, a success message will appear.

5. If you want to open the "Downloads" folder where the video was saved, click on the **Atvērt lejuplāžu mapi** (Open Downloads Folder) button. The tool will attempt to open the folder and highlight the downloaded video.

---

## How it works

- When you provide a YouTube video URL and click **Lejupielādēt video** (Download Video), the tool uses the `yt-dlp` library to fetch the video and save it to your "Downloads" folder in the best available quality (up to 1080p, MP4 format).
- The download runs in a separate thread to prevent the GUI from becoming unresponsive during the process.
- Once the download is complete, the path to the downloaded video is stored in a global variable, which allows the program to open the folder and highlight the file for you.

---

## Troubleshooting

- **Error in downloading**: If the download fails, ensure that the URL is correct and that the video is publicly available. The tool may not work with age-restricted or private videos.
- **Video not found in the Downloads folder**: Ensure that your `Downloads` directory is located in the default path under your user directory. If you've changed this, the video may be downloaded elsewhere.
- **Missing dependencies**: If you encounter an ImportError or similar issues, ensure that you have installed all the necessary libraries.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

If you wish to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

---

## Acknowledgments

- This tool relies on `yt-dlp`, a powerful open-source tool for downloading videos from YouTube and many other websites.
- The GUI is built with `tkinter`, Python's standard library for creating graphical interfaces.

---

If you have any questions or suggestions, feel free to open an issue on the GitHub repository!

