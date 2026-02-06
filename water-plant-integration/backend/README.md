# Water Plant Integration — Backend

E-Log module is implemented. SCADA, WIMS, and CMMS connectors can be added alongside.

## E-Log

- **REST API** (under `/api/elog`):
  - `POST /api/elog/entries` — create a log entry (operator, type, body, optional plant_id, metadata)
  - `GET /api/elog/entries/{id}` — get one entry
  - `GET /api/elog/entries` — list with filters: `plant_id`, `operator_id`, `entry_type`, `from_time`, `to_time`, `limit`, `offset`
  - `GET /api/elog/entry-types` — standard entry types (readings_approved, wo_created, alert_log_only, etc.)

- **Connector (for use inside the app)**  
  After WIMS sync or when creating a WO, call:
  - `elog.log_readings_approved(db, operator_id=..., plant_id=..., body=...)`
  - `elog.log_wo_created(db, operator_id=..., asset_name="Pump 3", wo_number=...)`
  - `elog.log_alert_only(db, operator_id=..., asset_name="Pump 3", alert_summary=...)`

- **Persistence:** SQLite (`elog.db` in the backend directory). Swap to Postgres by changing `database.py` and setting `DATABASE_URL`.

## Run

```bash
cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload
```

- API docs: http://127.0.0.1:8000/docs  
- Health: http://127.0.0.1:8000/health  

## Optional: forward to external E-Log

When you have an external E-Log product (e.g. Elogger) and its API spec, add an adapter in `elog/connector.py` that calls `create_entry()` for our DB and then posts the same payload to the external API.
