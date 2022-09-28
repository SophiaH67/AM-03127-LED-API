# AM-03127-LED-API

Just an API server for the AM-03127-LED matrix display.

## Setup

```bash
pip install fastapi uvicorn
```

Start the app by running

```bash
sudo chmod 0777 /dev/ttyUSB0
uvicorn main:app --reload --host 0.0.0.0
```
