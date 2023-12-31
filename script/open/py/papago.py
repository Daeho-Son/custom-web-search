import sys

from workflow import Workflow3


def get_data(word):
    url = 'https://papago.naver.com/'


def main(wf):
    args = wf.args[0]
    print(args)

    def wrapper():
        return get_data(args)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
