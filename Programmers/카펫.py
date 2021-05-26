def solution(brown, yellow):
    answer = []
    width = 3  # 3x3부터 적용 가능
    while True:
        height = (yellow / (width - 2)) + 2
        if int(height) == height:
            height = int(height)
            if (width + height - 2) * 2 == brown:
                if width < height:
                    width, height = height, width
                return [width, height]
        width += 1
    return answer
