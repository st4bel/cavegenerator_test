import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "mimimimimicanttellthekey"

    GRID_HEIGHT = 40
    GRID_WIDTH = 40
    START_ALIVE_CHANCE = 0.4
    STARVE_LIMIT = 3
    OVERPOP_LIMIT = 4
    MIN_POP_BIRTH = 3
    NUMBER_OF_STEPS = 5
