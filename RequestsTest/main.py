import requests

token = "9ca41f4703bd99da04ed832a179a998e"

response = requests.post('https://api.pokemonbattle.me:9104/pokemons',
                         json={
                            "name": "Vovch1k",
                            "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                            headers={"Content-Type":"application/json", "trainer_token": token})

print(response.text)

pokemon_id = response.json()["id"]

response = requests.put('https://api.pokemonbattle.me:9104/pokemons',
                         json={
                            "pokemon_id": pokemon_id,
                            "name": "Vovch1kNew",
                            "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                            headers={"Content-Type":"application/json", "trainer_token": token})

print(response.text)

pokemon_id = response.json()["id"]

response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                         json={
                          "pokemon_id": pokemon_id},
                            headers={"Content-Type":"application/json", "trainer_token": token})

print(response.text)

