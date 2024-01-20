def solution(s):
    words = s.split(" ")  # 문자열을 공백을 기준으로 나누어 리스트로 만듭니다.

    jaden_case_words = []
    for i, word in enumerate(words):
        if word:  # 단어가 공백이 아닌 경우에만 처리
            if word[0].isalpha():  # 단어의 첫 글자가 알파벳인 경우
                jaden_case_words.append(word[0].upper() + word[1:].lower())
            else:  # 단어의 첫 글자가 알파벳이 아닌 경우
                jaden_case_words.append(word.lower())

        # 공백을 추가 (마지막 단어 이후에는 공백을 추가하지 않음)
        if i < len(words) - 1:
            jaden_case_words.append(" ")

    result = "".join(jaden_case_words)  # 리스트로 변환된 단어들을 다시 문자열로 합칩니다.
    
    return result
