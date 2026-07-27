def main():
    print("Welcome to the AI Placement Journey!")
    print("This repository is a practice space for Python, DSA, ML, and projects.")

    topics = ["Python", "DSA", "Machine Learning", "Pandas", "Projects"]
    print("\nTopics to practice:")
    for topic in topics:
        print(f"- {topic}")

    progress = {"Python": 8, "DSA": 6, "Machine Learning": 5}
    print("\nCurrent progress:")
    for skill, level in progress.items():
        print(f"{skill}: {'$'* level}")


if __name__ == "__main__":
    main()
