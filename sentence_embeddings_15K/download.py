import requests

data_url = "https://raw.githubusercontent.com/jamescalam/data/main/sentence_embeddings_15K/"

for i in range(57):
    if i < 10:
        i = '0' + str(i)
    res = requests.get(data_url+f"embeddings_{i}.npy")
    with open(f'./data/embeddings_{i}.npy', 'wb') as fp:
        for chunk in res:
            fp.write(chunk)
    print('.', end='')