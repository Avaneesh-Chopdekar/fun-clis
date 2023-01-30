import os
import inquirer as inq
from pytube import YouTube

filename: str

# Download Video Function
def download(url: str, condition: str, filename: str, res: str):
    yt = YouTube(url)
    print("Downloading Video...")
    match condition:
        case "Highest Quality":
            yt = yt.streams.get_highest_resolution()
        case "Lowest Quality":
            yt = yt.streams.get_lowest_resolution()
        case "Audio Only":
            yt = yt.streams.get_audio_only()
        case "Custom Resolution":
            yt = yt.streams.get_by_resolution(res)
    try:
        # To save video in desktop directory
        home_directory = os.path.expanduser("~")
        path = os.path.join(home_directory, "Desktop")
        yt.download(output_path=path, filename=filename)
        if filename.endswith(".mp4"):
            print("Video downloaded successfully in your desktop.")
        else:
            print("Audio downloaded successfully in your desktop.")
    except:
        print("Error while download, Please try again.")

# To set filename variable
def set_filename(name: str):
    global filename
    filename = name


# Taking user input
questions = [
    inq.Text("url", message="Enter Youtube Video URL"),
    inq.List(
        "option",
        message="Enter an option to download the video",
        choices=[
            "Highest Quality",
            "Lowest Quality",
            "Audio Only",
            "Custom Resolution",
        ],
        default="Highest Quality",
    ),
]

answers = inq.prompt(questions)

# Validating if user wants to save as audio or video
if answers["option"] == "Audio Only":
    audio_filename_question = [
        inq.Text(
            "audio_filename",
            message="Enter filename with extension",
            default="audio.mp3",
        )
    ]
    audio_filename_answer = inq.prompt(audio_filename_question)
    set_filename(audio_filename_answer["audio_filename"])
else:
    video_filename_question = [
        inq.Text(
            "video_filename",
            message="Enter filename with extension",
            default="video.mp4",
        )
    ]
    video_filename_answer = inq.prompt(video_filename_question)
    set_filename(video_filename_answer["video_filename"])


# Validating if the user selects Custom Resolution
if answers["option"] == "Custom Resolution":
    custom_res_question = [inq.Text("res", message="Enter Resolution", default="720p")]
    custom_res_answer = inq.prompt(custom_res_question)
    download(answers["url"], answers["option"], filename, custom_res_answer["res"])
else:
    download(answers["url"], answers["option"], filename, "")
