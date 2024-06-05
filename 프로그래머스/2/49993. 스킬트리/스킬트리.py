def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        temp = ''
        for char in tree:
            if char in skill:
                temp += char
        if skill.startswith(temp):
            cnt += 1
            
    return cnt