class Human:
    def __init__(self,name, old, number, address, gender, email):
        self.name = name
        self.old = old
        self.number = number
        self.address =address
        self.gender = gender
        self.email = email
    def __str__(self):
        return f'name: {self.name}\n' \
            f'old: {self.old}'

class Guest(Human):
    def __init__(self,name, old):
        super().__init__(name, old, None, None, None, None)


class Player(Human):
    pass

#legit để chỉ tài khoản chưa được xác minh
class Legit:
    def __init__(self, github):
        self.github = github
        self.legit = False

class Developer(Human, Legit):
    pass


class GraphicDesginer(Human, Legit):
    pass
    

class SystemAdmin(Human, Legit):
    def set_legit(self, role):
        role = True



class Account:
    def __init__(self,username, password, role):
        self.username = username
        self.password = password
        self.role = role
    def create_role(self, role, *args, **kwargs):
     # Dựa trên tên role, tạo ra đối tượng tương ứng
        if role == "Player":
            return Player(*args, **kwargs)
        elif role == "Developer":
            return Developer(*args, **kwargs)
        elif role == "GraphicDesigner":
            return GraphicDesginer(*args, **kwargs)
        elif role == "SystemAdmin":
            return SystemAdmin(*args, **kwargs)
        else:
            raise ValueError(f"Role '{role}' không hợp lệ.")
        



    