from article import Article
from TheGuardianScraper import TheGuardianScraper
from BBCScraper import BBCScraper
import sys

websites = []

if len(sys.argv) == 1:
	websites = ["BBC", "TheGuardian"]

elif sys.argv[1] == "help":
	print("Run this script to scrape articles from the available websites. Currently TheGuardian and BBC are available. If you want to scrape only some of these websites, specify them as a command line argument")

else:
	websites = sys.argv[1:]


bbcscraper = BBCScraper()
guardianscraper = TheGuardianScraper()
if websites:
	if "BBC" in websites:
		bbcscraper.scrape_news()
	if "TheGuardian" in websites:
		guardianscraper.scrape_news()