"""Report question-bank coverage against the PMI July 2026 Exam Content Outline tasks.
Usage: python3 tools/coverage.py > question-bank/COVERAGE.md
Each task has a target; the gap column is the work queue for the next batch."""
import json, glob, collections, os
BASE = os.path.join(os.path.dirname(__file__), "..", "question-bank")
TARGET_TOTAL = 1000
DOMAINS = {
 "People": (0.33, ["Develop a common vision","Manage conflicts","Lead the project team","Engage stakeholders","Align stakeholder expectations","Manage stakeholder expectations","Help ensure knowledge transfer","Plan and manage communication"]),
 "Process": (0.41, ["Integrated plan and delivery","Scope","Value-based delivery","Resources","Procurement","Finance","Quality","Schedule","Evaluate project status","Closure"]),
 "Business Environment": (0.26, ["Governance","Compliance","Manage and control changes","Impediments and issues","Risk","Continuous improvement","Organizational change","External environment"]),
}
TOPIC_TO_TASK = {
 "vision":("People",0),"conflict":("People",1),"team":("People",2),"leadership":("People",2),"ethics":("People",2),
 "stakeholders":("People",3),"expectations":("People",5),"knowledge":("People",6),"communication":("People",7),
 "integrated":("Process",0),"scope":("Process",1),"value":("Process",2),"benefits":("Process",2),"resources":("Process",3),
 "procurement":("Process",4),"finance":("Process",5),"evm":("Process",5),"quality":("Process",6),"schedule":("Process",7),
 "agile":("Process",7),"status":("Process",8),"closure":("Process",9),
 "governance":("Business Environment",0),"compliance":("Business Environment",1),"sustainability":("Business Environment",1),
 "change":("Business Environment",2),"issues":("Business Environment",3),"risk":("Business Environment",4),
 "improvement":("Business Environment",5),"lessons":("Business Environment",5),"org change":("Business Environment",6),
 "external":("Business Environment",7),
}
have = collections.Counter(); unmapped = collections.Counter(); total = 0
for f in sorted(glob.glob(os.path.join(BASE, "bank*.json"))):
    for q in json.load(open(f)):
        total += 1
        m = TOPIC_TO_TASK.get(q.get("t"))
        if m: have[m] += 1
        else: unmapped[q.get("t")] += 1
print(f"# Coverage against the July 2026 outline\n\n{total} of {TARGET_TOTAL} questions written. Regenerate with `python3 tools/coverage.py`.\n")
for d,(w,tasks) in DOMAINS.items():
    per = TARGET_TOTAL * w / len(tasks)
    dom_have = sum(have[(d,i)] for i in range(len(tasks)))
    print(f"## {d} ({int(w*100)}%): {dom_have} of {int(TARGET_TOTAL*w)}\n\n| # | Outline task | Have | Target | Gap |\n| --- | --- | --- | --- | --- |")
    for i,t in enumerate(tasks):
        h = have[(d,i)]; tg = round(per)
        print(f"| {i+1} | {t} | {h} | {tg} | {max(0,tg-h)} |")
    print()
if unmapped: print("Unmapped topic tags:", dict(unmapped))
