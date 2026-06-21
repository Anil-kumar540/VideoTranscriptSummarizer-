from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id: str):
    """
    Function to get transcript and save the text values from each dict

    :param video_id: the full link of the video
    :type video_id: str
    """
    ls = YouTubeTranscriptApi().fetch(video_id)
    tx = [(d["text"] if isinstance(d, dict) else getattr(d, "text", "")) + " " for d in ls]
    # # ----------------------------------------------------------------------------
    with open("ms_kitco.txt", "w", encoding="utf-8") as f:
        f.write("".join(tx))
