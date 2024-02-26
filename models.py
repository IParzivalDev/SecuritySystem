class Camera:
    def __init__(self, id:int) -> None:
        self.id = id
        self.enabled = True

    def verify(self, image:list) -> bool | None:
        if self.enabled == True:
            for z in range(len(image)):
                for y in range(len(image[z])):
                    for x in range(len(image[z][y])):
                        if image[z][y][x] != None:
                            return True
            return False
        else:
            return None

    def turn_on(self) -> bool:
        self.enabled = True
        return self.enabled
    
    def turn_off(self) -> bool:
        self.enabled = False
        return self.enabled
    
    
class Passway:
    def __init__(self,id:int,cameras:list[Camera]) -> None:
        self.id = id
        self.cameras = cameras
        self.passway = [
            [[None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None]],

            [[None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None]],

            [[None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None]],

            [[None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None]],

            [[None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None]],

            [[None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None]],
        ]
    
    def verify(self):
        results = []
        for camera in range(len(self.cameras)):
            results.append((self.cameras[camera].id, self.cameras[camera].verify(self.passway)))

        return dict(results)

class Base:
    def __init__(self, passways:list[Passway]) -> None:
        self.passways = passways
        self.cameras:list[Camera] = []

        for passway in range(len(passways)):
            for camera in passways[passway].cameras:
                self.cameras.append(camera)

        self.security_system = True
        self.advanced_security_system = False
    
    def security_system_turn_on(self):
        for camera in range(len(self.cameras)):
            self.cameras[camera].turn_on()

        self.security_system = True
        return self.security_system
    
    def advanced_security_system_turn_on(self):
        self.advanced_security_system = True
        return self.advanced_security_system
    
    def verify_strangers(self):
        results = []
        for passway in range(len(self.passways)):
            results.append((self.passways[passway].id, self.passways[passway].verify()))

        results = dict(results)
        
        stranger = False

        for k, v in results.items():
            for k1, v1 in v.items():
                if v1 != None:
                    if v1 == True:
                        stranger = True
                        break
        
        return stranger, dict(results)