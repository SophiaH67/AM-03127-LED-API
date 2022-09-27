from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from message import DataPacket

html = """
<head>
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">
    <title>Rina-chan Board</title>
</head>
<a href="https://webcache.googleusercontent.com/search?q=cache:1IhlBpYkgeoJ:remy-manu.no-ip.biz/Afficheur/AM-03127-LED.pdf&cd=1&hl=en&ct=clnk&gl=nl&client=firefox-b-d
">Commands List</a><br>
<a href="https://cdn.discordapp.com/attachments/963356938526162994/1024229439858544670/EDZ111_Communication_ASCII_Protocol.pdf">In-Depth Protocol</a>
<form action="/" method="post">
    <input type="text" name="data">
    <input type="submit" value="Submit">
</form>
"""

static_files = [
    "android-chrome-192x192.png",
    "android-chrome-256x256.png",
    "apple-touch-icon.png",
    "browserconfig.xml",
    "favicon-16x16.png",
    "favicon-32x32.png",
    "favicon.ico",
    "mstile-150x150.png",
    "safari-pinned-tab.svg",
    "site.webmanifest",
]

for file in static_files:

    @app.get(f"/{file}")
    def get_file(file=file):
        return FileResponse(f"static/{file}")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return html


@app.post("/", response_class=HTMLResponse)
def post_root(data: str = Form()):
    packet = DataPacket(data)
    with open("/dev/ttyUSB0", "w") as f:
        f.write(str(packet))
        f.flush()
        f.close()
        print(f"Sent packet: {packet}")
    clean_packet = str(packet).replace("<", "&lt;").replace(">", "&gt;")
    return f"{html}<h2>Sent packet: {clean_packet}</h2>"
