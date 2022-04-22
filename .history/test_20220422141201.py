from TikTokApi import TikTokApi

# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
with TikTokApi() as api:
    print("start")
    for trending_video in api.trending.videos(count=50):
        print("test")
        # Prints the author's username of the trending video.
        print(trending_video.author.username)