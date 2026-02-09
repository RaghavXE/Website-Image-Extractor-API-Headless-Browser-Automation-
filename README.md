# Website Image Extractor API (Headless Browser Automation)

This is a **learning-focused backend project** built using **FastAPI** and **Playwright** to understand **headless browser automation** and dynamic web content handling.

The API launches a headless browser, navigates to a given website, and extracts image URLs rendered on the page.

⚠️ This project is created **for learning and experimentation purposes only** and is not intended for production scraping.

---

## What This Project Does

- Opens a website using a **headless Chromium browser**
- Handles JavaScript-rendered (dynamic) pages
- Extracts image URLs from the DOM
- Exposes the functionality via a simple REST API
- Demonstrates browser lifecycle: browser → context → page

---

## Why This Project?

This project was built to:
- Practice **Playwright fundamentals**
- Understand **headless browser workflows**
- Learn how browser automation integrates with APIs
- Gain hands-on experience with real website behavior

It serves as a **learning checkpoint**, not a production tool.

---

## Tech Stack

- **Python**
- **FastAPI** – backend API
- **Playwright** – headless browser automation
- **Pydantic** – request validation
- **Uvicorn** – ASGI server

---

## Project Structure

website-image-extractor-api/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore


---

## Installation & Setup

###  Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate # Windows
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Install Playwright browsers
```bash
playwright install
```
### Running the Application
```bash
uvicorn main:app --reload
```
Open your browser and visit:

http://127.0.0.1:8000/docs

## API Usage

Endpoint
POST /generate
Request Body
```bash
{
  "link": "https://example.com"
}
```
Sample Response
```bash
{
  "title": "Example Domain",
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ]
}
```
## Key Concepts Practiced
• Headless browser automation
• Page navigation and load strategies
• DOM element querying
• Image extraction logic
• API-driven automation
• Real-world website limitations

## ⚠️ Important Notes
### Some websites may block automated access
### Results may vary depending on site behavior

### This project does not attempt to bypass protections

### Built strictly for educational purposes

## 👤 Author
Built by Raghav as part of hands-on learning with FastAPI and Playwright.
