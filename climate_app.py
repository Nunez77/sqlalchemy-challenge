# Imports Dependencies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
import sqlalchemy

import datetime as dt
import numpy as np