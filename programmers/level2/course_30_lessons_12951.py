"""
    공백으로 분리(split)하여
    파이썬 내장함수를 사용하면 해결되는 간단한 문제
"""


def solution(s):
    split_data = s.split(' ')  # 공백을 기준으로 문자열을 나눔

    # capitalize 함수 설명
    # https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EB%AC%B8%EC%9E%90%EC%97%B4_capitalize()
    for idx, string in enumerate(split_data):
        split_data[idx] = split_data[idx].capitalize()

    return ' '.join(split_data)  # join을 이용하여 문자열을 합침


solution("3people unFollowed me")