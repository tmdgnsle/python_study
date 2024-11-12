# Base64 인코딩 테이블
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_decode(encoded_string):
    # 각 문자를 인덱스로 변환
    bit_string = ""
    for char in encoded_string:
        if char == "=":  # 패딩 문자 무시
            continue
        # 각 문자를 6비트 이진 문자열로 변환하여 연결
        bit_string += format(BASE64_ALPHABET.index(char), '06b')

    # 8비트씩 나누어 원래의 바이트 문자열로 변환
    decoded_bytes = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i + 8]
        if len(byte) == 8:  # 8비트가 안 되는 경우는 무시
            decoded_bytes.append(int(byte, 2))

    # 바이트 배열을 문자열로 변환하여 반환
    return decoded_bytes.decode('utf-8')


# 테스트 케이스 개수 입력 받기
T = int(input().strip())

# 각 테스트 케이스 입력 받고 디코딩하기
for t in range(1, T + 1):
    encoded_string = input().strip()
    # Base64 디코딩 수행
    decoded_string = base64_decode(encoded_string)

    # 결과 출력
    print(f"#{t} {decoded_string}")