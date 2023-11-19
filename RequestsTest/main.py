import requests

token = '694d32cf1895d8ca0a3d6a586bf6ecb7'
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}, headers = {'Content-Type': 'application/json'})'''


'''response_activation = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
    }, headers = {'Content-Type': 'application/json'})

print(response_activation.text)'''

'''response_change_trainer = requests.put(f'{host}/trainers', json = {    
    "name": "Vitamin",
    "city": "Tokyo"
}, headers = {'Content-Type': 'application/json', 
              'trainer_token': token})

print(response_change_trainer.text)'''

response_add_pokemon = requests.post(f'{host}/pokemons', json = {    
    "name": "dedushka",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})
 
print(response_add_pokemon.text)














