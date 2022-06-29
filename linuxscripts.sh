#!/bin/sh
pip3  install -r requirements.txt
echo "requirements are installed."
python3 project/init/init/db.py
echo "project is insitialized."
python3 runserver.py
echo "server is running."

