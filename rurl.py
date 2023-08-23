import re


def extract_urls(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf8') as file:
            with open(output_file, 'w') as out_file:
                for line in file.readlines():
                    if re.match(r'([a-zA-Z]{2,})+\.[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+', line):
                        out_file.write(line)
    except UnicodeDecodeError:
        with open(input_file, 'r', encoding='gbk') as file:
            with open(output_file, 'w') as out_file:
                for line in file.readlines():
                    if re.match(r'([a-zA-Z]{2,})+\.[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+', line):
                        out_file.write(line)
    except:
        print('报错辣!')


input_file = 'data.txt'
output_file = 'urls_out.txt'
extract_urls(input_file, output_file)
