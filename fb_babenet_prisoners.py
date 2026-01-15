import random
import time

def simulate_100_prisoners(n_simulations):
    """
    100명의 죄수 문제 시뮬레이션
    - Optimal Strategy: 자신의 번호에서 시작하여 상자 안의 번호를 따라가는 사이클 전략
    - Random Strategy: 각 죄수가 무작위로 50개의 상자를 선택하는 전략
    """
    
    optimal_success = 0
    random_success = 0
    
    print(f"시뮬레이션 시작 (시행 횟수: {n_simulations:,}회)...")
    start_time = time.time()

    # 1. 최적 전략(Optimal Strategy) 시뮬레이션
    for _ in range(n_simulations):
        drawers = list(range(100))
        random.shuffle(drawers)
        
        all_passed = True
        for prisoner in range(100):
            found = False
            current_drawer = prisoner
            for _ in range(50):
                card = drawers[current_drawer]
                if card == prisoner:
                    found = True
                    break
                current_drawer = card
            
            if not found:
                all_passed = False
                break
        
        if all_passed:
            optimal_success += 1

    # 2. 무작위 전략(Random Strategy) 시뮬레이션 
    # (수학적으로 성공 확률이 거의 0이므로 별도 루프로 짧게 시행)
    for _ in range(min(n_simulations, 10000)):
        drawers = list(range(100))
        random.shuffle(drawers)
        
        all_passed = True
        for prisoner in range(100):
            if prisoner not in random.sample(range(100), 50):
                all_passed = False
                break
        if all_passed:
            random_success += 1

    end_time = time.time()
    
    # 결과 출력
    print("-" * 50)
    print(f"최적 전략(Cycle Strategy) 성공 확률: {(optimal_success / n_simulations) * 100:.4f}%")
    print(f"무작위 전략(Random Strategy) 성공 확률: {(random_success / min(n_simulations, 10000)) * 100:.4f}%")
    print(f"총 소요 시간: {end_time - start_time:.2f}초")
    print("-" * 50)

if __name__ == "__main__":
    # 과제 요구사항인 100,000회 시행
    simulate_100_prisoners(100000)
