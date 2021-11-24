# 투포인터 방식

def solve(s: str) -> str:
    ans = ''

    def expend(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

    # 굳이 처리할 필요가 없을 때
    if len(s) < 2 or s == s[::-1]:
        return s

    for i in range(len(s) - 1):
        ans = max(ans, expend(i, i + 2), expend(i, i + 1), key=len)

    return ans


print(solve('babad'))
print(solve('cbbd'))
