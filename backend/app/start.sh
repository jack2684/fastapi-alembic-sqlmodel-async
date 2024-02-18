echo "Starting counta backend..."

alembic upgrade head
python app/initial_data.py
gunicorn -w 3 -k uvicorn.workers.UvicornWorker app.main:app \
  --bind 0.0.0.0:8000 \
  --preload --log-level=debug \
  --timeout 300