# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.8: Pandas - Data Analysis Working With DataFrame and Youtube Application
# python 4_8_youtube.py
blank = "----------------------"
import pandas as pd
import numpy as np

# Get Youtube Data using DataFrame and Pandas

# Milestone 1: Get first ten record
file = pd.read_csv("DEvideos.csv", encoding="UTF-8")
data_frame = pd.DataFrame(file)
first_ten = file.head(10)
print(f"M1 - First ten record:\n{first_ten}\n{blank}") 

##############################################################################################################

# Milestone 2: Get second five records
second_five = data_frame[5:10]
print(f"M2 - Second five record: {second_five}\n{blank}") 

##############################################################################################################

# Milestone 3: Get column names and amount
print(f"M3 - Column names and amount:\n") 
column_names = file.info()
column_names = data_frame.columns
column_len = len(data_frame.columns)
print(f"{blank}") 

##############################################################################################################

# Milestone 4: Remove unnecessarry columns
data_frame.drop(["video_id", "trending_date", "publish_time", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"], axis=1, inplace=True)
remove_columns = data_frame["title"]
print(f"M4 - Columns removed:\n{remove_columns}\n{blank}") 

##############################################################################################################

# Milestone 5: Get mean of likes and dislikes
like_mean = data_frame["likes"].mean()
dislike_mean = data_frame["dislikes"].mean()
print(f"M5 - Means: \nLike mean:{like_mean}\nDislike mean: {dislike_mean}\n{blank}") 

##############################################################################################################

# Milestone 6: Get dislike and like columns for first 50 records
first_fifty_like = file[["title","likes"]].head(50)
first_fifty_dislike = file[["title","dislikes"]].head(50)
print(f"M6 - First 50: \nFirst 50 like column:\n{first_fifty_like}\n{blank}\nFirst 50 dislike column:\n{first_fifty_dislike}\n{blank}") 


##############################################################################################################

# Milestone 7: Get the best video
best = data_frame["views"].max()
the_best = data_frame[data_frame["views"] == best][["title","views","likes","dislikes"]]
print(f"M7 - The best video is:\n{the_best}\n{blank}")

##############################################################################################################

# Milestone 8: Get the worst video
worst = data_frame["views"].min()
the_worst = data_frame[data_frame["views"] == worst][["title","views","likes","dislikes"]]
print(f"M8 - The worst video is:\n{the_worst}\n{blank}")

##############################################################################################################

# Milestone 9: Get top ten videos
top_ten = data_frame.nlargest(n=10, columns=["views"])[['title','views']]
# top_ten = data_frame.sort_values("views", ascending=False)[["title","views","likes","dislikes"]]
print(f"M9 - Top ten videos are:\n{top_ten}\n{blank}")

##############################################################################################################

# Milestone 10: Get average likes as sorted according to category ID
like_id_sorting = data_frame.groupby("category_id").mean().sort_values("likes")["likes"]
print(f"M10 - Average likes as sorted according to category ID:\n{like_id_sorting}\n{blank}") 

##############################################################################################################

# Milestone 11: Get comment numbers as sorted according to category ID
comments = data_frame.groupby("category_id").sum().sort_values("comment_count", ascending=False)
print(f"M11 - comment numbers as sorted according to category ID:\n{comments}\n{blank}") 

##############################################################################################################

# Milestone 12: How many videos there are per category?
video_amount = data_frame["category_id"].value_counts()
print(f"M12 - Video amount per category:\n{video_amount}\n{blank}") 

##############################################################################################################

# Milestone 13: Generate a new column for title length
data_frame["title_len"] = data_frame["title"].apply(len)
print(f"M13 - Title lenght column:\n{data_frame}\n{blank}") 

##############################################################################################################

# Milestone 14: Generate a new column for tag numbers
data_frame["tag_amount"] = data_frame["tags"].apply(lambda x: len(x.split('|'))) 
print(f"M14 - Tag number column:\n{data_frame}\n{blank}") 

##############################################################################################################

# Milestone 15: List most popular videos according to likes and dislikes

# popular = data_frame.nlargest(n=10, columns=["likes"])[['title','likes', 'dislikes', 'views',]]

def ratio(dataset):
    like_list = list(dataset["likes"])
    dislike_list = list(dataset["dislikes"])
    listing = list(zip(like_list, dislike_list))

    ratio_list = []

    for like,dislike in listing:
        if(like + dislike) == 0:
            ratio_list.append(0)
        else:
            ratio_list.append((like/(like+dislike))*100)
    return ratio_list

data_frame["Like_ratio"] = ratio(data_frame)
popular = data_frame.sort_values('Like_ratio', ascending=False)
print(f"M15 - The most popular ones:\n{popular}\n{blank}")