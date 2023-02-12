def recur(n, cnt):
    h = '_' * cnt * 4
    cnt += 1
    if not n:
        print(h + chat[0])
        print(h + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(h + chat_end)
        return
    else:
        for i in range(4):
            print(h + chat[i])
        recur(n-1, cnt)
        print(h + chat_end)

chat = ['"재귀함수가 뭔가요?"', '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
chat_end = '라고 답변하였지.'
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recur(int(input()), 0)