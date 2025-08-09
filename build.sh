#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies (opcional, pode ser removido se já estiver no render.yaml)
pip install -r requirements.txt

# Run migrations (opcional, já configurado para rodar como um worker no render.yaml)
# python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
