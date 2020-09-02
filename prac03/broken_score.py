"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = int(input("Enter score: "))
    print(user_score(score))

def user_score(score):
    if score <= 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        return "Bad"

main()