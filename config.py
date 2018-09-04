import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "mimimimimicanttellthekey"

    GRID_HEIGHT = 20
    GRID_WIDTH = 20
    START_ALIVE_CHANCE = 0.6
    STARVE_LIMIT = 1
    OVERPOP_LIMIT = 4
    MIN_POP_BIRTH = 2
    NUMBER_OF_STEPS = 1
