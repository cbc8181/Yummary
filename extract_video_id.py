import re

# def extract_video_id_from_url(url):
#     pattern = re.compile(
#         r'.*(?:youtu.be\/|v\/|u\/\w\/|embed\/|watch\?.*&?v=)([^#&?]*).*', re.IGNORECASE)
#     match = pattern.search(url)
#     if match and len(match.group(1)) == 11:  # Checking if the extracted ID is of correct length
#         return match.group(1)
#     return None  # If there is no match, return None

def extract_video_id_from_url(url):
    regex = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None
