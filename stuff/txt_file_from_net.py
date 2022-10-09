from urllib import request

goog_url = "http://www.sample-videos.com/text/Sample-text-file-10kb.txt"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\n")
    dst_url = r'dwn.txt'
    fw = open(dst_url,'w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()


download_stock_data(goog_url)
