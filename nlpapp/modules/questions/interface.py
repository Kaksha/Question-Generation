from .appos_which_where_qts import WhichWhere
from .howqts import How
from .noqts import No
from .obj_who_qts import ObjWho
from .sub_who_qts import SubWho
from .what_qts import What
from .whereqts import Where
from .yes_qts import Yes


class QuestionInterface:
    def __init__(self):
        self.questions = {
            # 'which': WhichWhere(''),
            'how': How(''),
            'no': No(''),
            'obj_who': ObjWho(''),
            'sub_who': SubWho(''),
            'what': What(''),
            'where': Where(''),
            'yes': Yes(''),
        }

        self.options = [k for k in self.questions.keys()]

    def __repr__(self):
        print('<<Interface object for questions>>')

    def get_text(self, text, option):
        return self.questions[option].modify_and_get_text(text)

if __name__ == '__main__':
    q = QuestionInterface()
    print('print some shit')
    t = input()
    for option in q.options:
        print('{} - {}'.format(option, q.get_text(input(), option)))