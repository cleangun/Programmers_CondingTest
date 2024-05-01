def solution(orders):
    answer = 0
    for order in orders:
        if ("americano" in order) or ("anything" in order):
            answer += 4500
        elif "cafelatte" in order:
            answer += 5000
    return answer