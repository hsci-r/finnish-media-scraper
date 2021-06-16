from setuptools import setup, find_packages

with open('README.md') as fp:
    README = fp.read()

setup(
    name='finnish_media_scrapers',
    version='0.1.0',
    author='Human Sciences - Computing Interaction Research Group',
    author_email='eetu.makela@helsinki.fi',
    description='Scrapers for extracting articles from Finnish journalistic media websites.',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages('src', exclude=['tests', 'tests.*']),
    package_dir={'': 'src'},
    test_suite='tests',
    install_requires=['urllib3', 'lxml','requests==2.25.1','beautifulsoup4','selenium'],
    entry_points={
        'console_scripts' : [
            'fms-query-yle = finnish_media_scrapers.scripts.query_yle:main',
            'fms-query-il = finnish_media_scrapers.scripts.query_il:main',
            'fms-query-is = finnish_media_scrapers.scripts.query_is:main',
            'fms-query-hs = finnish_media_scrapers.scripts.query_hs:main',
            'fms-fetch-hs = finnish_media_scrapers.scripts.fetch_hs:main',
            'fms-fetch-open = finnish_media_scrapers.scripts.fetch_open:main',
            'fms-html-to-text-yle = finnish_media_scrapers.scripts.htmltotext_yle:main',
            'fms-html-to-text-svyle = finnish_media_scrapers.scripts.htmltotext_svyle:main',
            'fms-html-to-text-il = finnish_media_scrapers.scripts.htmltotext_il:main',
            'fms-html-to-text-is = finnish_media_scrapers.scripts.htmltotext_is:main',
            'fms-html-to-text-hs = finnish_media_scrapers.scripts.htmltotext_hs:main',
            'fms-post-filter = finnish_media_scrapers.scripts.post_filter:main'
        ]
    }
)


