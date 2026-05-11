from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser

fm = FileManager("students.csv")
if not fm.check_file():
    print("Stopping program.")
    exit()
fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

print("\n------------------------------")
print("Running all analysers:")
print("------------------------------")

analysers = [GpaAnalyser(dl.students), CountryAnalyser(dl.students)]
for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

saver = ResultSaver(analysers[0].result, "output/result.json")
report = Report(analysers[0], saver)
report.generate()
