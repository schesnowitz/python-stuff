
class ADD_FILE:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
        
    def get_name(self):
        return self.name
        
        
    def GET_FILE_SIZE(self):
        return self.size    
        
        
    def __repr__(self) -> str:
        return f"{self.name} {self.size}"   
            

f = ADD_FILE("/file.txt","10")
print(f)
print(f.GET_FILE_SIZE())

print("hello")
