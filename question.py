
class Question:
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

test = [
    '1+3=?  \na)1\nb)2\nc)3\nd)4\n\n',
    '9×y=108？\na)972\nb)99\nc)117\nd)12\n\n',
    '下面哪一種物質會流動？\na)雪\nb)雨\nc)冰\nd)霜\n\n',
    '哪一種果實裡只有一顆種子？\na)榴槤\nb)櫻桃\nc)臺灣欒樹\nd)柳丁\n\n'
]

questions=[
    Question(test[0],"d"),
    Question(test[1],"d"),
    Question(test[2],"b"),
    Question(test[3],"b"),
    ]

def run(questions):
    score = 0
    for question in questions:
        answer = input(question.description + '輸入你的答案:')
        if answer == question.answer:
            score +=1
    print('得到' + str(score) + '分')
    
    
run(questions)


