#!/bin/sh
while ! `nc -z chrome 4444`; do sleep 3; done
mkdir -p /worker/LOG
python3 test.py
python3 run.py --headless --superfast --currency CNY  --no-images --dont-check-for-updates --telegram 6270857753:AAFbDeYq17uryI1VcLO-4KIDN5A3gE9jImA 5167458750 >> LOG/log-`date +"%F"`.txt
python3 run.py --headless --superfast --currency CNY --no-images --start-at 08:00 --everyday --dont-check-for-updates --telegram 6270857753:AAFbDeYq17uryI1VcLO-4KIDN5A3gE9jImA 5167458750 >> LOG/log-`date +"%F"`.txt
