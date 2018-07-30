#!/usr/bin/env bash
echo "========================================"
date
. ../env/bin/activate
cd /home/sendtank/app
./manage.py push_sync > /home/sendtank/logs/phone_sync.log