#!/bin/sh
wget https://raw.githubusercontent.com/TheManyHatsClub/v3nari/main/update.py
python3 update.py
echo "updated"
rm -rf update.py
