# This class is responsible for creating the data for the aircraft database.
# The created csv is stored in the db directory.
# This csv can be imported theough the admin section of the Django app.
# After clicking the Aircraft database, there will be an import button at the top right.

# To create the csv from scratch, the program uses these commands in order:

# a.cache_aircraft_data() - Store data from sources into cache.
# a.clean_data() - Clean data to fit into database.
# a.create_aircraft_db_csv() - Create csv from data.

# You can comment out the functions in __main__ depending on your needs.

#--ISSUES--#
# - Some sectors are stored in aircraft name. Example: Antonov An-148 (241 nmi).
# - These need to be changed after importing to the database.
# - At time of writing, it's currently only seven entries.
'''
## [1.0.0] - 2024-03-04
### Added
- a.cache_aircraft_data() - Store data from sources into cache.
- a.clean_data() - Clean data to fit into database.
- a.create_aircraft_db_csv() - Create csv from data.
### Changed
- csv is created with ids now.
'''

import os
import re
import time
import pandas as pd

# Various sources from wikipedia
aircraft_src = 'https://en.wikipedia.org/wiki/List_of_commercial_jet_airliners'
data_src = 'https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft'

aircraft_db_path = 'db/aircraft_db.csv'
aircraft_paths = ['cache/in_production.csv', 'cache/out_production.csv']
data_paths = [
    'cache/commuter.csv', 'cache/regional.csv', 'cache/short.csv',
    'cache/medium.csv', 'cache/long.csv'
]


def clean_text(text):
  text = str(text)
  text = re.sub(',', '', text)
  text = text.split()
  return text[0]


class Aircraft_Database:

  def __init__(self):
    pass

  def set_aircraft(self):
    return pd.read_csv(aircraft_paths[0])

  def create_aircraft_db_csv(self):
    for path in data_paths:
      if not os.path.isfile(path):
        print("ERROR: File not found:", path)
        print("Exiting without populating database...")
        return

    timestamp = time.time()
    new_path = aircraft_db_path.replace('.csv', f'_{timestamp}' + '.csv')

    print("Creating aircraft database csv...")
    with open(new_path, 'w') as f1:
      f1.write('model,seats,sector,fuelburn,fuelperseat\n')
      for path in data_paths:
        with open(path, 'r') as f2:
          f2.readline()
          f1.write(f2.read())
        f2.close()

    f1.close()

    print("Creation successful. Storing in:", new_path)
    df = pd.read_csv(new_path)
    df.to_csv(new_path, index=True, index_label='id')

  def clean_data(self):
    print("Cleaning Data...")
    for path in data_paths:
      df = pd.read_csv(path)
      if path == 'cache/commuter.csv':
        sector = pd.Series(['300'] * len(df))
        df.insert(3, 'Sector', sector)
      elif path == 'cache/short.csv':
        df.columns = df.columns.str.replace('Fuel Burn', 'Fuel burn')
        sector = pd.Series(['1000'] * len(df))
        df.insert(3, 'Sector', sector)
        df.columns = df.columns.str.replace('Fuel efficiency per seat',
                                            'Fuel per seat')
      elif path == 'cache/regional.csv':
        df.columns = df.columns.str.replace('Fuel efficiency per seat',
                                            'Fuel per seat')

      df['Fuel burn'] = df['Fuel burn'].apply(clean_text)
      df = df.drop(columns=['First flight'])
      df['Fuel per seat'] = df['Fuel per seat'].apply(clean_text)
      df['Sector'] = df['Sector'].apply(clean_text)
      df.to_csv(path, index=False)

  def cache_aircraft(self):
    print('Storing data for commercial airplanes from:', aircraft_src)
    data_dfs = pd.read_html(aircraft_src, header=0)
    for x in range(0, 2):
      df = data_dfs[x * 2]
      df.to_csv(aircraft_paths[x], index=False)

  def cache_data(self):
    print('Storing aircraft data from:', data_src)
    data_dfs = pd.read_html(data_src, header=0)
    for x in range(1, 6):
      df = data_dfs[x]
      df.to_csv(data_paths[x - 1], index=False)

  def cache_aircraft_data(self):
    self.cache_aircraft()
    self.cache_data()


if __name__ == "__main__":
  a = Aircraft_Database()

  #--Functions--#
  #a.cache_aircraft_data()
  #a.clean_data()
  a.create_aircraft_db_csv()
