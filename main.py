from models import Base, Camera, Passway
import time
import random


passways = [
    Passway(
        0,
        [
            Camera(0),
            Camera(1),
            Camera(2),
            Camera(3),
        ],
    ),
    Passway(
        1,
        [
            Camera(4),
            Camera(5),
            Camera(6),
            Camera(7),
        ],
    ),
    Passway(
        2,
        [
            Camera(8),
            Camera(9),
            Camera(10),
            Camera(11),
        ],
    ),
    Passway(
        3,
        [
            Camera(12),
            Camera(13),
            Camera(14),
            Camera(15),
        ],
    ),
]


base = Base(passways)


while True:
    if base.advanced_security_system == False:
        stranger = base.verify_strangers()[0]
        if stranger == True:
            base.advanced_security_system_turn_on()
        else:
            print("- ...")
            if random.random() < 0.2:
                passways[0].passway[0][0][0] = "Extraño"
    else:
        print("ADVERTENCIA: Alguien está en la empresa.")
    time.sleep(1)