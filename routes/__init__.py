from flask import Blueprint

clients_bp = Blueprint('clients', __name__)

from .clients import *