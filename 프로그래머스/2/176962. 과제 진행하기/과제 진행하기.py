from datetime import datetime, timedelta

def solution(plans):
    wait = []
    answer = []
    
    # 시간이 빠른 순으로 정렬
    plans = sorted(plans, key=lambda x: x[1])
    
    # 예정된 계획이 있는 동안 진행
    while plans:
        turn_class = plans.pop(0)
        
        # 다음 예정된 과제가 있다면
        if len(plans) > 0:
            nowTime = datetime.strptime(turn_class[1], "%H:%M")
            nextTime = datetime.strptime(plans[0][1],"%H:%M")
            finishTime = nowTime + timedelta(minutes=int(turn_class[2]))
            
            # 다 끝낼 수 없다면
            if finishTime > nextTime:
                delta_diff = finishTime - nextTime
                delta_diff_minutes = delta_diff.total_seconds() // 60
                wait.append([turn_class[0] , delta_diff_minutes])
            # 다 끝냈을때 (+ 시간이 남았을때)
            else:
                # 예정된 일정 완료
                answer.append(turn_class[0])
                # 다 못끝낸 항목들 시간이 될때 해두기
                while wait:
                    last_wait_class = wait.pop()
                    finishTime += timedelta(minutes=last_wait_class[1])
                    if finishTime > nextTime:
                        delta_diff2 = finishTime - nextTime
                        delta_diff_minutes2 = delta_diff2.total_seconds() // 60
                        wait.append([last_wait_class[0] , delta_diff_minutes2])
                        break
                    else:
                        answer.append(last_wait_class[0])
            
        # 예정된 과제가 없다면
        else:
            answer.append(turn_class[0])
            
    # 아직 다 못끝낸 과제가 있다면
    while wait:
        turn_waitClass = wait.pop()
        answer.append(turn_waitClass[0])
    
    
    return answer