class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = [float(s["GPA"]) for s in self.students]
        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": sum(1 for g in gpas if g > 3.5),
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        super().print_results()
        print("-" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        counts = {}
        for s in self.students:
            c = s["country"]
            counts[c] = counts.get(c, 0) + 1
        top3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
        self.result = {
            "total_countries": len(counts),
            "top_3": top3,
            "all_countries": counts,
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("Country Analysis")
        print("-" * 30)
        print(f"total_countries: {self.result['total_countries']}")
        print("Top 3 Countries:")
        for i, (country, count) in enumerate(self.result["top_3"], 1):
            print(f"  {i}. {country} : {count}")
        print("-" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
