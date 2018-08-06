
def second(**kwargs):
    print(kwargs)

def first(**kwargs):
    print(kwargs)
    second(**kwargs)






first(hello='bye',hi='goodbay')


