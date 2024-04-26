def solution(chicken):
    answer = 0
    
    while chicken // 10 >= 1:
        coupon = chicken // 10
        chicken = (chicken - coupon * 10) + coupon
        answer += coupon
    
    
    
    
    return answer