from db.repository import SqlRepository
from parser.adsparser import AdsParser

parser = AdsParser()
result = parser.get_ads_from_pages(1, 30)
repository = SqlRepository()
repository.print_version()
print("To save: ", len(result))
for i, key in enumerate(result):
    repository.save_ads(result.get(key))
