import os

for item in os.listdir("J:/static/movies"):
    eitem = str(item).replace(" ", "-")
    os.rename(str("J:/static/movies/"+item), str("J:/static/movies/"+eitem))
    print(str(item)+" turned into "+eitem)
else:
    print("Files done")