from bing_image_downloader import downloader

########### ADAPTAR ###############
numberImages=100
queries = ["prato de comida brasileira"]  

for query_string in queries:
    downloader.download(query_string, 
                    limit=numberImages, 
                    output_dir='bingImages',
                    adult_filter_off=True, 
                    force_replace=False, 
                    timeout=60)