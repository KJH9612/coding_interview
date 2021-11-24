"""
    딕셔너리와 리스트를 이용해 간단하게 풀 수 있는 문제
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemon_name_dict = dict()
pokemon_list = []

for i in range(n):
    pokemon_name = sys.stdin.readline().rstrip()    # 포켓몬 이름 입력받음
    pokemon_name_dict[pokemon_name] = i + 1         # key : 포켓몬 이름, value : 입력받은 순서
    pokemon_list.append(pokemon_name)               # list에 포켓몬의 이름을 저장

for i in range(m):
    find_value = sys.stdin.readline().rstrip()      # 찾을 포켓몬 이름 또는 번호를 입력받음
    get_value = ''                                  # 출력하기 위해 만든 변수
    if find_value.isdigit():                        # 입력받은 값이 숫자이면
        get_value = pokemon_list[int(find_value) - 1]   # list에 넣어둔 포켓몬 이름 출력
    else:
        get_value = pokemon_name_dict[find_value]       # dict에 넣어둔 포켓몬의 value를 출력

    print(get_value)
