import random

def load_questions_and_answers():
    with open("Q.txt", "r", encoding="utf-8") as q_file:
        questions = q_file.readlines()
    
    with open("A.txt", "r", encoding="utf-8") as a_file:
        answers = a_file.readlines()
    
    # 질문과 답을 각각 줄바꿈 제거 후 반환
    questions = [q.strip() for q in questions]
    answers = [a.strip() for a in answers]
    
    return questions, answers

def normalize_answer(answer):
    """정답을 표준화하여 비교 가능하도록 변환"""
    if answer.startswith("~"):
        # 물결(~)을 제외한 뒤 쉼표로 구분된 각 항목을 집합으로 처리
        answer_variations = answer[1:].lower().replace(" ", "").split(",")
        normalized_answers = set(answer_variations)  # 집합으로 반환
    else:
        # 물결(~)이 없으면 그대로 순서에 맞게 리스트로 처리
        # 콜론(:)을 구분자로 처리하여 :로 구분된 항목을 동일한 정답으로 취급
        answer_variations = answer.lower().replace(" ", "").replace(":", ",").split(",")
        normalized_answers = answer_variations  # 리스트로 반환
    
    return normalized_answers

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

def quiz_program():
    print_welcome_message()  # 시작 시 안내 메시지 출력
    
    questions, answers = load_questions_and_answers()
    
    # 문제들을 랜덤하게 섞기
    combined = list(zip(questions, answers))
    random.shuffle(combined)  # 문제와 답을 섞는다.
    questions, answers = zip(*combined)  # 섞인 문제와 답을 다시 분리
    
    score = 0
    total = len(questions)
    
    for i in range(total):
        print(f"문제 {i+1}: {questions[i]}")
        correct_answers = normalize_answer(answers[i])  # 정답 정규화
        
        attempts = 3  # 최대 3번의 기회 제공
        while attempts > 0:
            user_answer = input(f"답을 입력하세요 ({attempts}번 남음, Q 입력 시 종료, J 입력 시 스킵): ").strip().lower().replace(" ", "")
            user_answer_list = user_answer.split(",")  # 쉼표로 구분하여 리스트로 처리

            # 사용자가 'Q'나 'ㅂ'를 입력하면 종료
            if user_answer.upper() == "Q" or user_answer == "ㅂ":
                print("퀴즈를 종료합니다.")
                print(f"\n총 {score} / {total} 문제를 맞추셨습니다.")
                return
            
            # 사용자가 'J'나 'ㅏ'를 입력하면 문제를 스킵
            if user_answer.upper() == "J" or user_answer == "ㅓ":
                print(f"틀렸습니다. 정답은 \"{answers[i]}\" 입니다. (문제를 스킵했습니다.)\n")
                break

            # 정답이 집합인 경우(물결(~) 포함): 순서 상관없이 비교
            if isinstance(correct_answers, set):
                if set(user_answer_list) == correct_answers:
                    print("정답입니다! \n")
                    score += 1
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"틀렸습니다. 다시 시도하세요. ({attempts}번 남음)")
                    else:
                        print(f"!!틀렸습니다. 정답은 \"{answers[i]}\" 입니다. \n")
            # 정답이 리스트인 경우(물결(~) 미포함): 순서대로 비교
            else:
                if user_answer_list == correct_answers:
                    print("정답입니다! \n")
                    score += 1
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"틀렸습니다. 다시 시도하세요. ({attempts}번 남음)")
                    else:
                        print(f"!!틀렸습니다. 정답은 \"{answers[i]}\" 입니다. \n")
    
    print(f"\n총 {score} / {total} 문제를 맞추셨습니다.")

if __name__ == "__main__":
    quiz_program()
