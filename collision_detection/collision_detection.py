# Copyright (c) GearDragon Software 2016
class Collider(object):
    def set_coords(self, x=0, y=0, width=0, height=0, anchor="center"):
        if len(anchor) == 2:
            if anchor[0] == 'n':
                self.y1 = y
                self.y2 = y + height
            elif anchor[0] == 's':
                self.y1 = y - height
                self.y2 = y
            else:
                raise Exception("Invalid anchor")
            
            if anchor[1] == 'w':
                self.x1 = x
                self.x2 = x + width
            elif anchor[1] == 'e':
                self.x1 = x - width
                self.x2 = x
            else:
                raise Exception("Invalid anchor")
        else:
            self.x1 = x - width / 2
            self.x2 = x + width / 2 + width % 2
            self.y1 = y - height / 2
            self.y2 = y + height / 2 + height % 2
