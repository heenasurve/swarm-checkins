import json

categories = dict();
files = [
    'data/checkins_2022.json',
    'data/checkins_2021_SH.json',
    'data/checkins_2021_FH.json',
    'data/checkins_2020_SH.json',
    'data/checkins_2020_FH.json'
]

for file in files:
    with open(file) as f:
        checkins = json.load(f);


    for checkin in checkins:
        for category in checkin['venue']['categories']:
            catKey = category['pluralName']
            if catKey not in categories:
                categories[catKey] = 1
            else:
                categories.update({catKey : categories.get(catKey)+1})

    f.close();

for key,value in categories.items():
    print(key , ':', value)
