#!/usr/bin/env python3

import json
import argparse
import inspect
import sys
import os
import io
import base64
import aiohttp
import urllib
import asyncio
import aiofiles
import aioconsole
import logging
import re, concurrent.futures, configparser, motor.motor_asyncio, ssl, zipfile
import blitzutils as bu
from blitzutils import WG
from blitzutils import WoTinspector

logging.getLogger("asyncio").setLevel(logging.DEBUG)
FILE_CONFIG 	= 

DEBUG 	= False
VERBOSE = False
SLEEP 		= 2
MAX_RETRIES = 3
REPLAY_N 	= 0
SKIPPED_N 	= 0
ERROR_N 	= 0
WIurl='https://wotinspector.com/api/replay/upload?'
WG_appID  = 'c688c996873daa7657609b096c46dfe7'
wg = None
wi = None
