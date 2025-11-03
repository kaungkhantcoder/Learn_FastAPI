from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTORNIC = 'electornic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electornic'},
    {'id': 3, 'name': 'Black Sabbath', 'genre': 'Metal'},
    {'id': 4, 'name': 'Win-Tang Clan', 'genre': 'Hip-Hop'},
]

@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band Not Found")
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]

@app.post('/bands/genre')
async def create_genre():
    pass

# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(item_id: int):
#     """
#     Deletes an item from the database based on its ID.
#     Returns a 204 No Content status on successful deletion,
#     or a 404 Not Found if the item does not exist.
#     """
#     if item_id not in items_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Item with ID {item_id} not found"
#         )
#     del items_db[item_id]
#     # No content to return for a successful DELETE operation (204 No Content)
#     return