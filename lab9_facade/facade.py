"""Implementation of the Builder pattern"""


class VideoConverter:
    def convert(self, video_file, target_format):
        """The logic of video conversion into the required format"""
        pass


class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def upload_video(self, video_data):
        """The logic of uploading videos to YouTube using the API"""
        pass


class YouTubeUploaderFacade:
    def __init__(self, api_key):
        self.video_converter = VideoConverter()
        self.youtube_api = YouTubeAPI(api_key)

    def upload_video(self, video_file, target_format):
        """Uploading videos to YouTube"""
        converted_video = self.video_converter.convert(video_file, target_format)
        self.youtube_api.upload_video(converted_video)


if __name__ == '__main__':
    api_key = "YOUR_API_KEY"
    facade = YouTubeUploaderFacade(api_key)

    video_file = "video.some_type"
    target_format = "mp4"

    facade.upload_video(video_file, target_format)
