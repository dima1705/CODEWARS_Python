# def lovefunc( flower1, flower2):
#     if flower1 % 2 == 0 and flower2 % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lovefunc(1,4)


def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)