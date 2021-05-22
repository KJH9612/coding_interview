def solution(maps):
    answer = 0
    n_len = len(maps)
    m_len = len(maps[0])

    if not maps[n_len - 2][m_len - 1] or not maps[n_len - 1][m_len - 2]:
        return -1

    return answer