#!/bin/bash
gunicorn3 -w 24 -b 0.0.0.0:65535 -k gevent server:app
