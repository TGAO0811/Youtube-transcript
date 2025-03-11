from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(youtube_url):
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

def get_captions(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL!"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        captions = "\n".join([entry["text"] for entry in transcript])
        return captions
    except Exception as e:
        return f"Error fetching captions: {str(e)}"

video_link = input('Enter the YouTube video URL: ')
captions = get_captions(video_link)
print(captions)
