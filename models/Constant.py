import enum

# Class enum sử dụng hằng số
class Status(enum.Enum):
    freeze = 'freeze'
    die = 'die'
    move = 'move'
    attack = 'attack'

arr_random_status_soldier = [Status.freeze, Status.attack, Status.move]

# class Status_Hero(enum.Enum):
#     freeze = {'name': 'freeze', 'count':3}
#     die = {'name': 'die', 'count':19}
#     move = {'name': 'move', 'count':4}
#     attack = {'name': 'attack', 'count':4}

class Direction(enum.Enum):
    left = 'left'
    right = 'right'