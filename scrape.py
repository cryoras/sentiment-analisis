from google_play_scraper import reviews_all, Sort
import csv
import pandas as pd

scrapreview = reviews_all(
    'com.tokopedia.tkpd',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=5000
)

with open('ulasan_aplikasi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrapreview:
        writer.writerow([review['content']])

app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.shape
app_reviews_df.head()

df = app_reviews_df[['userName', 'score', 'content']]
df.to_csv('Tokopedia.csv', index=False)
