from itertools import product

def solution(u, e):
    discount_rates = [10,20,30,40]
    # 이모티콘 개별 할인율의 모든 조합 구하기
    discount_cases = list(product(discount_rates, repeat=len(e)))
    
    cases = []
    # 조합 for문
    for c_idx in range(len(discount_cases)):
        comb_cnt , comb_sum = 0, 0
        discount_case = discount_cases[c_idx]
        # user for문
        for u_idx in range(len(u)):
            user_limit_discount , user_limit_price = u[u_idx][0] , u[u_idx][1]
            user_price = 0;
            # discount for문
            for d_idx in range(len(discount_case)):
                # 유저가 원하는 할인율일 경우
                if discount_case[d_idx] >= user_limit_discount:
                    user_price += (e[d_idx] * (100 -discount_case[d_idx])) // 100
            
            if user_price >= user_limit_price:
                comb_cnt += 1
            else:
                comb_sum += user_price
                
        cases.append([comb_cnt, comb_sum])
    
    cases = sorted(cases , key = lambda x: (x[0],x[1]), reverse=True)
    
    answer = cases[0]
    return answer