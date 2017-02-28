# -*- coding: utf-8 -*-

# Scrapy settings for ForumCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import time

BOT_NAME = 'ForumCrawler'

SPIDER_MODULES = ['ForumCrawler.spiders']
NEWSPIDER_MODULE = 'ForumCrawler.spiders'

JOBDIR = 'job'
DOWNLOAD_TIMEOUT = 30

# Logging
LOG_PATH = 'log'
LOG_FILE = LOG_PATH + '/' + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + '.log'
LOG_LEVEL = 'INFO'

# MySQL
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = '960423'
MYSQL_DB = '1point3acres'
MYSQL_CHARSET = 'utf8'
# TABLE_INFO: pk, fk refer to primary key and foreign key, they must be iterable
TABLE_INFO = {
    'board': {
        'attrs': {
            'board_url': 'varchar(100)',
            'board_name': 'nvarchar(40)',
            'pages': 'int',
        },
        'pk': ('board_url',),
        'engine': 'MyISAM',
    },

    'post': {
        'attrs': {
            'post_url': 'varchar(100)',
            'post_name': 'nvarchar(100)',
            'board_url': 'nvarchar(100)',
            'board_name': 'nvarchar(40)',
            'user_url': 'varchar(100)',
            'user_name': 'nvarchar(30)',
            'replies': 'int',
            'pv': 'int',
            'date_time': 'datetime',
            'content': 'text',
            'context': 'text',
        },
        'pk': ('post_url',),
        'engine': 'MyISAM',
    },

    'user': {
        'attrs': {
            'user_url': 'varchar(100)',
            'uid': 'int',
            'user_name': 'nvarchar(30)',
            'profile': 'text',
        },
        'pk': ('user_url',),
        'engine': 'MyISAM',
    },
}

ITEM_PIPELINES = {
    'ForumCrawler.pipelines.MySQLPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ForumCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_ITEMS = 512

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
# COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'ForumCrawler.middlewares.ForumCrawlerMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ForumCrawler.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
