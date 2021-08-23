from utils import load_filters


class AbstractScraper:
    filters = load_filters.load_filters()

    def process(self):
        print('Started to scrape {}'.format(self.get_name()))
        data = []
        links = self.fetch_links()
        for link in self.apply_filter(links, self.filters):
            try:
                print(link)
                processed = self.process_link(link)
                data.append(processed)
            except Exception as e:
                print('Failed to process {}, error: {}'.format(link, str(e)))
        return data

    def get_name(self):
        raise NotImplementedError('Abstract method must be implemented')

    def fetch_links(self):
        raise NotImplementedError('Abstract method must be implemented')

    def apply_filter(self, data, filters):
        raise NotImplementedError('Abstract method must be implemented')

    def process_link(self, link):
        raise NotImplementedError('Abstract method must be implemented')
