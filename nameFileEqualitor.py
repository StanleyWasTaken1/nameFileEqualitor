
import os

path = '/scraping/scrapy/projects/realestate/realestate/spiders'
for file in os.listdir(path):
    if file.endswith('.py'):
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as f:
            content = f.read()
            if 'name' in content:
                name_line = content.split('name')[1].split('\n')[0]
                spider_name = name_line.replace('=', '').replace('"', '').replace("'", "").strip()
                file_base_name = file[:-3]
                if spider_name != file_base_name:
                    print(f'UPSÍÍ! File: "{file}"')
                    print(f'Soubor = "{file_base_name}" | name = "{spider_name}"\n')
