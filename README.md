# PokeDB Scraper
🔥🔥A pokemonDB scraper for all info about pokemon 🔥🔥



## Purpose
This is my own project as I want to create pokemon apps but cannot find a good pokemon API. The original website is [pokemondb.net](pokemondb.net)



### How to Use

1. Scrape pokemon status. Use below command for scraping the basic pokemon list with their own status. It will generate two file `PokemonData.json` and `pokedex`.

   ```
   python stats_scrape.py
   ```

   

2. Get all image based on pokemon list data from `pokedex`. It will create new folder as container of all image that will be downloaded. (PS. there is still some bug because I need to check all image list manually with their source)

   ```
   python image_scrape.py
   ```



### Note

This is just an example work of web scrapper and not guarantee 100% will work. 

