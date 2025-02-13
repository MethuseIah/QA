import random

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def print_welcome_message():
    """프로그램 시작 시 안내 메시지 출력"""
    welcome_message = """
 ---------------------------------------------------------------
|           @@@ 모듈 교재 정리본 문답 프로그램    @@@          |
|           @@@ 여러 정답입력시 ','로 구분합니다. @@@          |
|           @@@ 공백, 대소문자 상관 없습니다.     @@@          |
|    -- 위대한 고기정 강사님의 지원을 받아 작성되었습니다 --   |
|           모듈 교재 정리해준 전*호님 감사합니다.             |                                     
|           문제와 정답은 수정이 가능합니다.                   |                                     
|                                                # made by JSY |
 ---------------------------------------------------------------
"""
    print(welcome_message)

def compare_answers(correct_answer, user_answer, is_order_sensitive):
    # 콜론(:)으로 구분된 정답을 그룹화 (소문자로 변환)
    correct_groups = [[opt.lower().strip() for opt in group.split(':')] for group in correct_answer.split(',')]
    user_list = [ans.lower().strip() for ans in user_answer.split(',')]

    # 각 그룹에서 사용자 답이 하나라도 포함되어 있는지 확인
    for user_ans in user_list:
        found = False
        for group in correct_groups:
            if user_ans in group:
                found = True
                break
        if not found:
            return False

    # 순서가 중요한 경우, 사용자 답의 순서와 그룹 순서가 일치해야 함
    if is_order_sensitive:
        for i, user_ans in enumerate(user_list):
            if user_ans not in correct_groups[i]:
                return False
    return True

def main():
    questions = read_file('Q.txt')
    answers = read_file('A.txt')

    if len(questions) != len(answers):
        print("문제와 정답의 개수가 일치하지 않습니다.")
        return
    
    print_welcome_message()
    
    # 문제들을 랜덤하게 섞기
    combined = list(zip(questions, answers))
    random.shuffle(combined)  # 문제와 답을 섞는다.
    questions, answers = zip(*combined)  # 섞인 문제와 답을 다시 분리
    
    total_questions = len(questions)
    solved_questions = 0

    for i, (question, correct_answer) in enumerate(zip(questions, answers)):
        print(f"\n문제 {i+1}/{total_questions}: {question}")
        attempts = 3  # 최대 3번 시도 가능

        # 물결표(~)가 있는지 확인하여 순서 중요 여부 결정
        is_order_sensitive = not correct_answer.startswith('~')
        if not is_order_sensitive:
            correct_answer = correct_answer[1:]  # 물결표 제거

        while attempts > 0:
            user_answer = input("답을 입력하세요 (Q: 종료, J: 스킵): ")

            # 종료 처리
            if user_answer.lower() in ['q', 'ㅂ']:
                print("프로그램을 종료합니다.")
                return

            # 스킵 처리
            if user_answer.lower() in ['j', 'ㅓ']:
                print("문제를 스킵합니다.\n")
                print(f"정답은 {correct_answer}입니다.\n")
                break

            # 정답 비교 (대소문자 구분 없음)
            if compare_answers(correct_answer, user_answer, is_order_sensitive):
                print("정답입니다!\n")
                solved_questions += 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"틀렸습니다. 다시 시도해보세요. (남은 기회: {attempts}번)")
                else:
                    print(f"틀렸습니다. 정답은 {correct_answer}입니다.\n")

    print(f"총 {total_questions}문제 중 {solved_questions}문제를 풀었습니다.")

if __name__ == "__main__":
    main()      
    
