import sys


'''
    replace를 사용하면 시간초과
    
def processing_bomber(target: str, boom: str) -> str:
    while True:
        if len(target) == 0:
            return 'FRULA'
        find_check = target.find(boom)
        if find_check != -1:
            target = target.replace(boom, '')
        elif find_check == -1:
            return target
'''


target_str = sys.stdin.readline().rstrip()
boom_str = sys.stdin.readline().rstrip()

'''print(processing_bomber(target_str, boom_str))'''