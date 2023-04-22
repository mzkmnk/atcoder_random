import requests
import random
import webbrowser

def get_atcoder_problems():
    url = "https://kenkoooo.com/atcoder/resources/problems.json"
    response = requests.get(url)
    return response.json()

def select_random_problems(problems, count_per_difficulty):
    selected_problems = {}
    for difficulty in ['A', 'B', 'C', 'D','E']:
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

if __name__ == "__main__":
    main()
