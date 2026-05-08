from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main():
    file_path = "data/student.xlsx"

    df = pd.read_excel(file_path)
    df["평균점수"] = df[["영어점수", "수학점수"]].mean(axis=1)

    print("전체 데이터:")
    print(df)

    row_count, column_count = df.shape

    print()
    print(f"행 개수: {row_count}")
    print(f"열 개수: {column_count}")

    english_average = df["영어점수"].mean()
    math_average = df["수학점수"].mean()
    study_time_average = df["주당평균공부시간"].mean()
    sleep_time_average = df["주당평균수면시간"].mean()

    print()
    print("평균값 분석 결과")
    print("=" * 30)
    print(f"영어점수 평균: {english_average:.2f}")
    print(f"수학점수 평균: {math_average:.2f}")
    print(f"주당평균공부시간 평균: {study_time_average:.2f}")
    print(f"주당평균수면시간 평균: {sleep_time_average:.2f}")

    top_students = df.sort_values(by="평균점수", ascending=False).head(3)

    print()
    print("평균점수 상위 3명")
    print("=" * 30)
    print(top_students[["이름", "영어점수", "수학점수", "평균점수"]].to_string(
        index=False,
        formatters={"평균점수": "{:.2f}".format},
    ))

    english_study_corr = df["영어점수"].corr(df["주당평균공부시간"])
    math_study_corr = df["수학점수"].corr(df["주당평균공부시간"])
    english_sleep_corr = df["영어점수"].corr(df["주당평균수면시간"])
    math_sleep_corr = df["수학점수"].corr(df["주당평균수면시간"])

    print()
    print("상관계수 분석 결과")
    print("=" * 30)
    print(f"영어점수와 주당평균공부시간 상관계수: {english_study_corr:.3f}")
    print(f"수학점수와 주당평균공부시간 상관계수: {math_study_corr:.3f}")
    print(f"영어점수와 주당평균수면시간 상관계수: {english_sleep_corr:.3f}")
    print(f"수학점수와 주당평균수면시간 상관계수: {math_sleep_corr:.3f}")

    result_dir = Path("result")
    result_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(8, 6))
    plt.scatter(df["주당평균공부시간"], df["평균점수"])
    plt.title("Study Hours vs Average Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Average Score")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(result_dir / "study_vs_avg_score.png")
    plt.show()


if __name__ == "__main__":
    main()

