#!/bin/bash

cd ahmia

scrapy crawl ahmia-tor -s FULL_PAGERANK_COMPUTE=False -s LOG_LEVEL=DEBUG