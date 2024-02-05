def solution(text, ending):
    return True if ending == text[-(len(ending)):] else False


##### v2
# def solution(string, ending):
#     return string.endswith(ending)

print(solution('text', 'xt'))