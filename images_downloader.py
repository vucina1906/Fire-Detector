from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'fire_backyard3'})
google_crawler.crawl(keyword='fire backyard', max_num=50)
