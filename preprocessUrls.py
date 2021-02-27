

### combine all url.txt files com google scrapy ####

# import os
# with os.scandir("./googleImagesReverseSearch") as it:
#     allUrls = []
#     for entry in it:
#         print(entry.path)
#         with open(entry.path) as f:
#             content = f.readlines()
#             print(len(content))
#             allUrls += content
        
#     with open('./allUrls.txt', 'w') as f:
#         for item in allUrls:
#             f.write("%s" % item)


### remove duplicate lines ####

# with open('./googleReverseSearchUrls.txt', 'r') as f:
#     content = f.readlines()
#     print(len(content))
#     noDuplicationContent = set(content)
#     print(len(noDuplicationContent))
#     with open('./googleReverseSearchNoDuplication.txt', 'w') as f2:
#         for item in noDuplicationContent:
#             f2.write("%s" % item)


### compare two files and check how many of them are repeated ####

with open('./googleReverseSearchNoDuplication.txt', 'r') as f:
    contentReverse = f.readlines()
    print(len(contentReverse))
    with open('./googleAndBingUrlsNoDuplication.txt', 'r') as f2:
        content = f2.readlines()
        print(len(content))
        intersection = list(set(content) & set(contentReverse))
        print(len(intersection))
        