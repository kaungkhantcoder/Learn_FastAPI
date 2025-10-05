from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genere': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genere': 'Electornic'},
    {'id': 3, 'name': 'Slowdive', 'genere': 'Shoegaze'},
    {'id': 4, 'name': 'Win-Tang Clan', 'genere': 'Hip-Hop'},
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

@app.get('bands/genere/{genere}')
async def bands_for_genere(genere: str) -> list[dict]:
    return [
        b for b in BANDS if b['genere'].lower() == genere.lower()
    ]