print("hello,world")

def greet():
    print("こんにちは")
    
def print_name(name):
    print(f"私の名前は{name}です")
    
def get_greet():
    return "おはようございます"

def add(a,b):
    return a+b

result=add(3,5)
print(result)

git add example.py

git commit -m "Add example.py with basic Python functions"
git push
    
