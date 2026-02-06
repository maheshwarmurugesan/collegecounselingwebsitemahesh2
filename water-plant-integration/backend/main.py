"""Water Plant Integration API — E-Log and future connectors."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import init_db, get_session
from elog.routes import router as elog_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # shutdown if needed


app = FastAPI(
    title="Water Plant Integration API",
    description="Middleware: SCADA, WIMS, E-Log, CMMS. E-Log module included.",
    version="0.1.0",
    lifespan=lifespan,
)

# Mount E-Log under /api for consistency
app.include_router(elog_router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}
