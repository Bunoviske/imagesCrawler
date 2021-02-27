from bing_image_downloader import downloader

########### ADAPTAR ###############
numberImages= 200
queries = ["prato de comida","prato de comida brasileira","prato de arroz com feijao","prato de arroz integral com feijao","marmita pf","prato feito","prato com legumes","dieta prato","prato vegetariano","prato gorduroso","prato italiano","fatia de pizza no prato","prato de comida brasileira vista superior","prato de comida vista de cima"]  

for query_string in queries:
    downloader.download(query_string, 
                    limit=numberImages, 
                    output_dir='bingImages',
                    adult_filter_off=True, 
                    force_replace=False, 
                    timeout=60)