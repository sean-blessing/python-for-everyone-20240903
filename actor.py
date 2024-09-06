from dataclasses import dataclass

@dataclass
class Actor:
    firstName: str = ""
    lastName: str = ""
    birthYear: int = 0

    # return a string representing this Actor
    def getDetails(self):
        return (f"Actor: firstName: {self.firstName}, " 
               f"lastName: {self.lastName}, "
               f"birthYear: {self.birthYear}")