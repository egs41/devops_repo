#!/bin/bash
export FLASK_ENV=production

echo "Starting User Management Application..."
echo "Current time: $(date)"

mkdir -p /tmp

echo "Starting signup service on port 5000..."
python signup_app.py &
SIGNUP_PID=$!

echo "Starting list service on port 5001..."
python list_app.py &
LIST_PID=$!

echo "Signup service PID: $SIGNUP_PID"
echo "List service PID: $LIST_PID"

trap 'echo "Terminating services..."; kill $SIGNUP_PID $LIST_PID; exit 0' SIGTERM SIGINT

wait