
from extract_video_id import extract_video_id_from_url
from get_captions import *;

try:
    # test_url = 'https://www.youtube.com/watch?v=c3qu51WuKHA'
    # # test_url = 'https://www.youtube.com/watch?v=P-ERfVGn6ss'
    test_url = 'https://www.youtube.com/watch?v=SEykKJu3W8A'
    video_id = extract_video_id_from_url(test_url)
    captions = get_captions_list(video_id)
    captions_id = get_captions_id(captions)

    # captions_ids = 'AUieDabi7MlVfhlOiIeiJdvD3ie8wKBrr1KOXmSklkM_6kZKHFM'
    # captions_file = download_captions(captions_id)
    # if(captions_file is not None):
    #       # save the result to a file
    #     with open(f'{captions_id}.txt', 'w') as file:
    #         file.write(captions_file.text)


except Exception as e:
    print(f'Error: {e}')
