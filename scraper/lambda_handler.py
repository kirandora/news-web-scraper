from multiprocessing.dummy import Pool
from indianexpress_rs_scraper import IndiaExpressScraper
from thehindu_rs_scraper import TheHinduScraper
import time


def handle(event, context):
    start = time.time()
    print('Scraping started')
    pool = Pool(1)
    res = [pool.apply_async(TheHinduScraper().process)]
    pool.close()
    pool.join()
    end = time.time()
    print('Scraping took {} seconds'.format((end - start)))
    start = time.time()
    print('Started to write scraped data to database')
    for async_res in res:
        # publish data to kafka topic
        print("The response from process {}".format(async_res.get()))
        publish_to_kafka_topic('topic_name', async_res.get())
    print('Finished writing data to database, operation took {} seconds'.format((time.time() - start)))


def publish_to_kafka_topic(topic, items):
    pass


if __name__ == "__main__":
    handle(None, None)
