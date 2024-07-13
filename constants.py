# Constants - don't change
X = 510
Y = 552
BORDER_SIZE = 10
AVATAR_SIZE = 80
VEL = 4
ASSET_FOLDER = 'Assets/'
HOUSE_FILEPATH = 'Assets/House_background.png'

class Character:
    name: str
    avatar_filepath: str
    avatar_filepath_left: str
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.avatar_filepath = "Assets/" + name + ".png"
        self.avatar_filepath_left = "Assets/" + name + "_Left.png"
        
