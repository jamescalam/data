import requests
import os

data_url = "https://raw.githubusercontent.com/jamescalam/data/main/sentence_embeddings_15K/"

# create data directory to store data
if not os.path.exists('./data'):
    os.mkdir('./data')

# download the numpy binary files (dense vectors)
for i in range(57):
    if i < 10:
        i = '0' + str(i)
    res = requests.get(data_url+f"embeddings_{i}.npy")
    with open(f'./data/embeddings_{i}.npy', 'wb') as fp:
        for chunk in res:
            fp.write(chunk)
    print('.', end='')

# and download the respective text file
res = requests.get(f"{data_url}sentences.txt")
with open(f"./data/sentences.txt", 'wb') as fp:
    for chunk in res:
        fp.write(chunk)