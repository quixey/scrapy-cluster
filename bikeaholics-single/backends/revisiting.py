

from frontera.contrib.backends.sqlalchemy import revisiting
from frontera.core.components import Queue as BaseQueue, States


class Backend(revisiting.Backend):

    def _schedule(self, requests):

        # same
        batch = []
        for request in requests:
            import logging
            # if request.url == "http://www.bikeaholics.org/ALoop.html":
            #    import pdb; pdb.set_trace()
            #    logging.info("SCHEDULE: {}".format(request.url))

            if request.meta[b'state'] in [States.NOT_CRAWLED]:
                request.meta[b'crawl_at'] = revisiting.utcnow_timestamp()
            elif request.meta[b'state'] in [States.CRAWLED, States.ERROR]:
                # Feature: Allow the spider to specify the revisit date by adding a datetime to request.meta['crawl_at'];
                if b'spiderdate' in request.meta["scrapy_meta"]:
                    # import pdb; pdb.set_trace()
                    request.meta[b'crawl_at'] = request.meta[b"scrapy_meta"][b'spiderdate']
                    del request.meta[b'scrapy_meta'][b"spiderdate"]
                else:
                    request.meta[b'crawl_at'] = revisiting.utcnow_timestamp() + self.interval
            else:
                continue    # QUEUED
            batch.append((request.meta[b'fingerprint'], self._get_score(request), request, True))

        # same
        self.queue.schedule(batch)
        self.metadata.update_score(batch)
        self.queue_size += len(batch)
