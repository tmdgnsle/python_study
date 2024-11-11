T = int(input())  # 테스트 케이스 수 입력

for t in range(1, T + 1):
    N = int(input())  # 일 수 입력
    prices = list(map(int, input().split()))  # 매매가 입력

    max_profit = 0
    max_price = 0  # 뒤에서부터 현재까지의 최대 매매가

    # 뒤에서부터 매매가 탐색
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            max_profit += max_price - price

    print(f"#{t} {max_profit}")