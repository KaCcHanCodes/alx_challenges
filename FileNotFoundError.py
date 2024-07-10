try:
    file = open('README.me')
except FileNotFoundError:
    print("File does not exist")
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()