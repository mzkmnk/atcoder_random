"""
これはatcoderの過去問であるABCの問題をランダムに選んでブラウザで開くスクリプトです。
18行目にある['A', 'B', 'C', 'D','E']のリストを変更することで、選択する難易度を変更できます。
コードを自由に改変したり、改変したコードを公開しても構いません。
最近DDoSでUnratedになっていてモチベが下がっている人(自分も含め)や、問題を選ぶのが面倒な人は
このスクリプトを使ってみてください！！
またEx問題をリストに入れても表示されない？ので修正できたらします、、、笑
"""


import requests
import random
import webbrowser
import time

def get_atcoder_problems():
    url = "https://kenkoooo.com/atcoder/resources/problems.json"
    response = requests.get(url)
    return response.json()

def select_random_problems(problems, count_per_difficulty):
    selected_problems = {}
    for difficulty in ['A', 'B', 'C', 'D','E','F','G','Ex']:
        filtered_problems = [
            problem for problem in problems
            if problem['contest_id'].startswith('abc') and problem['id'].split('_')[-1].startswith(difficulty.lower())
        ]
        if len(filtered_problems) >= count_per_difficulty:
            selected_problems[difficulty] = random.sample(filtered_problems, count_per_difficulty)
        else:
            print(f"難易度 {difficulty} の問題が不足しています。")
    return selected_problems

def main():
    problems = get_atcoder_problems()
    selected_problems = select_random_problems(problems, 1)

    for difficulty, problem_set in selected_problems.items():
        if problem_set:
            problem_url = f"https://atcoder.jp/contests/{problem_set[0]['contest_id']}/tasks/{problem_set[0]['id']}"
            print(f"{difficulty}問題: {problem_url}")
            webbrowser.open(problem_url)
            time.sleep(2)

if __name__ == "__main__":
    main()
