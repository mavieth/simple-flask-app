import sys

sys.path.append('./')
from app import app

print("\nBlue prints\n--------------")
for blueprint in app.blueprints:
    print("Blueprint: {}".format(blueprint))
print("--------------")