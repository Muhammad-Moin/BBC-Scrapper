from Scrapper import Scrapper
from fastapi import FastAPI


app = FastAPI()
obj = Scrapper()

@app.get("/json")
def read_root(url):
    return obj.bbc_scrapper(url)
