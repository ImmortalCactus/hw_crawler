from crawler import Crawler
from args import get_args
import csv

if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    content = crawler.crawl(args.start_date, args.end_date)
    # TODO: write content to file according to spec
    with open(args.output, 'w', encoding= 'utf-8') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['date','title','content'])
        for row in content:
            csv_out.writerow(row)
