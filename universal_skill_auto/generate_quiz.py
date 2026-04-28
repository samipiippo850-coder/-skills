def make_quiz(input_md, output="quiz.md"):
    with open(input_md, "r", encoding="utf-8") as f:
        content = f.read()
    with open(output, "w", encoding="utf-8") as out:
        for i in range(1, 11):
            out.write(f"### Question {i}\n")
            out.write("**Question (EN/中):**\n\n")
            out.write("**Answer:**\n\n")
            out.write("**Explanation:**\n\n\n")
    print(f"Generated quiz template to {output}")

if __name__ == "__main__":
    md_file = input("Enter Markdown file to generate quiz from: ")
    make_quiz(md_file)