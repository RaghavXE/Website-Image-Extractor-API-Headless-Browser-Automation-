from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from playwright.sync_api import sync_playwright

app = FastAPI()

class Req(BaseModel):
    link: str

@app.post("/generate")
def gen(r: Req):
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        
        ctx = b.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1366, "height": 768},
            locale="en-US"
        )
        
        page = ctx.new_page()
        page.goto(r.link, timeout=60000)
        page.wait_for_load_state("networkidle")
        title = page.title()
        
        imgs = page.query_selector_all("img")
        img_urls = []
        
        for i in imgs:
            src = i.get_attribute("src")

            if src and "http" in src:
                img_urls.append(src)
        b.close()
        
    return {
        "title":title,
        "images": img_urls[:10]
    }
