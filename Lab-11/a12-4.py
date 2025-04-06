import pandas as pd

data = {
    'artist': ['ArtistA', 'ArtistB', 'ArtistA', 'ArtistC', 'ArtistB', 'ArtistA', 'ArtistC'],
    'venue': ['Venue1', 'Venue2', 'Venue2', 'Venue1', 'Venue1', 'Venue2', 'Venue2'],
    'date': ['2023-01', '2023-01', '2023-02', '2023-02', '2023-03', '2023-03', '2023-03']
}
concerts = pd.DataFrame(data)
# print(concerts)
counts = concerts.groupby(['artist', 'venue', 'date']).size().reset_index(name='count')
print("\nConcert Counts:")
# print(counts)

artists = concerts['artist'].unique()
venues = concerts['venue'].unique()

cross_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])
cross_df = pd.DataFrame(index=cross_pairs).reset_index()
# print(cross_df)

all_combinations = pd.merge(cross_df.assign(key=0), pd.DataFrame(concerts['date'].unique(), columns=['date']).assign(key=0), on='key').drop('key', axis=1)
full_counts = pd.merge(all_combinations, counts, on=['artist', 'venue', 'date'], how='left').fillna({'count': 0})

full_counts['artist_venue'] = full_counts['artist'] + '_' + full_counts['venue']

wide_table = full_counts.pivot(index='date', columns='artist_venue', values='count').fillna(0)
print(wide_table)