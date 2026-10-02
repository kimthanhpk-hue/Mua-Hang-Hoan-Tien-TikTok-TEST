from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="Mua Hang Hoan Tien - TikTok TEST")


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>TikTok TEST</title>
        </head>
        <body>
            <h2>Mua Hang Hoan Tien - TikTok TEST</h2>
            <p>Server is running.</p>
            <p>TikTok callback endpoint is ready.</p>
        </body>
    </html>
    """


@app.get("/tiktok/callback", response_class=HTMLResponse)
async def tiktok_callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")

    return f"""
    <html>
        <head>
            <title>TikTok Authorization</title>
        </head>
        <body>
            <h2>TikTok authorization callback received</h2>
            <p>Authorization code received: {"Yes" if code else "No"}</p>
            <p>State received: {"Yes" if state else "No"}</p>
        </body>
    </html>
    """
