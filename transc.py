from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    RequestBlocked,
    TranscriptsDisabled,
    NoTranscriptFound
)

def get_transcript(video_id: str):
    """
    Function to get transcript and save the text values from each dict

    :param video_id: the full link of the video
    :type video_id: str
    """
    try:
        ls = YouTubeTranscriptApi().fetch(video_id)
        tx = [(d["text"] if isinstance(d, dict) else getattr(d, "text", "")) + " " for d in ls]
        text = "".join(tx)
        
        # Save to file as previously done
        with open("ms_kitco.txt", "w", encoding="utf-8") as f:
            f.write(text)
            
        return True, text
        
    except RequestBlocked:
        return False, "YouTube temporarily blocked transcript access from this cloud server IP. Please try another video or try again later."
    except TranscriptsDisabled:
        return False, "This video does not have captions enabled."
    except NoTranscriptFound:
        return False, "No transcript available for this video in the required language."
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"
