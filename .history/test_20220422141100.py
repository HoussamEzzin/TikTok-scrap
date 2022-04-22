from TikTokApi import TikTokApi

api = TikTokApi()

for video in api.trending.videos(count=50):
    print("found")
    print(video.author.username)