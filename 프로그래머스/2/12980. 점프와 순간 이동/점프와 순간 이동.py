def solution(n):
    battery = 0  # 건전지 사용량
    while n > 0:
        # 현재 위치가 홀수면 건전지 사용량 1 증가
        if n % 2 == 1:
            battery += 1
            n -= 1  # 현재 위치를 한 칸 앞으로 이동
        else:
            n //= 2  # 순간이동
    return battery


