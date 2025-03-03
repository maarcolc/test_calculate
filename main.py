from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.position import Position
from typing import List

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

data_store: List[Position] = []

@app.get("/")
def index():
    return "server is running"

@app.post("/calculate")
async def calculate(position: Position):
    data_store.append(position)

    initial_margin = (position.entry_price * position.quantity) / position.leverage
    if position.position.lower() == "long":
        pnl = (position.entry_price - position.stop_loss) * position.quantity
    else:
        pnl = (position.stop_loss - position.entry_price) * position.quantity
    pnl_percentage = (pnl / initial_margin * position.quantity) * 100
    roi = (pnl / initial_margin) * 100

    return {
        "Margen inicial": initial_margin,
        "PnL": pnl,
        "PnL %": pnl_percentage,
        "ROI": roi,
    }
