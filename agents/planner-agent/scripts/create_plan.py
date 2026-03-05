#!/usr/bin/env python3
\"\"\"Generate structured plans from task descriptions.

Creates detailed plans following the Planner Agent methodology.
\"\"\"

import json
import sys
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    \"\"\"A single task in a plan.\"\"\"
    name: str
    description: str = ""
    completed: bool = False
    estimate_hours: float = 0.0
    
@dataclass
class Phase:
    \"\"\"A phase containing multiple tasks.\"\"\"
    name: str
    tasks: List[Task] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    estimate_hours: float = 0.0

@dataclass  
class Plan:
    \"\"\"A complete project plan.\"\"\"
    title: str
    goal: str
    phases: List[Phase] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    created: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_markdown(self) -> str:
        \"\"\"Convert plan to markdown format.\"\"\"
        lines = [
            f"# {self.title}",
            "",
            f"**Goal:** {self.goal}",
            "",
            "## Phases",
            ""
        ]
        
        total_hours = 0
        for phase in self.phases:
            phase_hours = sum(t.estimate_hours for t in phase.tasks)
            total_hours += phase_hours
            
            lines.append(f"### {phase.name} ({phase_hours}h)")
            lines.append("")
            for task in phase.tasks:
                status = "[x]" if task.completed else "[ ]"
                desc = f" - {task.description}" if task.description else ""
                lines.append(f"- {status} {task.name}{desc}")
            lines.append("")
        
        lines.extend([
            "## Summary",
            "",
            f"- Total Estimate: {total_hours} hours",
            f"- Phases: {len(self.phases)}",
            f"- Tasks: {sum(len(p.tasks) for p in self.phases)}",
            "",
            "## Risks",
            ""
        ])
        
        for risk in self.risks:
            lines.append(f"- {risk}")
        
        return "\n".join(lines)

def create_feature_plan(
    title: str,
    goal: str,
    features: List[str]
) -> Plan:
    \"\"\"Create a feature implementation plan.\"\"\"
    
    # Default phases for feature work
    phases = [
        Phase(
            name="Setup",
            tasks=[
                Task("Initialize project", estimate_hours=1),
                Task("Configure environment", estimate_hours=1),
                Task("Setup dependencies", estimate_hours=0.5),
            ],
            estimate_hours=2.5
        ),
        Phase(
            name="Core Implementation",
            tasks=[
                Task(f, estimate_hours=4) for f in features
            ],
            estimate_hours=len(features) * 4
        ),
        Phase(
            name="Testing",
            tasks=[
                Task("Write unit tests", estimate_hours=2),
                Task("Integration tests", estimate_hours=2),
                Task("Manual testing", estimate_hours=1),
            ],
            estimate_hours=5
        ),
        Phase(
            name="Polish",
            tasks=[
                Task("Code review", estimate_hours=1),
                Task("Documentation", estimate_hours=2),
                Task("Deployment", estimate_hours=1),
            ],
            estimate_hours=4
        )
    ]
    
    return Plan(
        title=title,
        goal=goal,
        phases=phases,
        risks=[
            "Requirements may change",
            "Integration complexity",
            "Performance issues",
        ]
    )

def create_bug_fix_plan(
    title: str,
    description: str
) -> Plan:
    \"\"\"Create a bug fix plan.\"\"\"
    
    phases = [
        Phase(
            name="Reproduce",
            tasks=[
                Task("Create minimal reproduction", estimate_hours=0.5),
                Task("Document reproduction steps", estimate_hours=0.25),
                Task("Verify environment", estimate_hours=0.25),
            ],
            estimate_hours=1
        ),
        Phase(
            name="Investigate",
            tasks=[
                Task("Find root cause", estimate_hours=2),
                Task("Analyze affected areas", estimate_hours=1),
            ],
            estimate_hours=3
        ),
        Phase(
            name="Fix",
            tasks=[
                Task("Implement fix", estimate_hours=1),
                Task("Write regression test", estimate_hours=0.5),
                Task("Test locally", estimate_hours=0.5),
            ],
            estimate_hours=2
        ),
        Phase(
            name="Deploy",
            tasks=[
                Task("Code review", estimate_hours=0.5),
                Task("Merge", estimate_hours=0.25),
                Task("Deploy and verify", estimate_hours=0.25),
            ],
            estimate_hours=1
        )
    ]
    
    return Plan(
        title=f"Fix: {title}",
        goal=description,
        phases=phases,
        risks=[
            "Root cause may be complex",
            "Fix may affect other components",
            "May need architectural changes",
        ]
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_plan.py <type> [args]")
        print("Types: feature, bug")
        print()
        print("Examples:")
        print("  python create_plan.py feature 'Payment Processing' 'Add Stripe' 'Handle refunds'")
        print("  python create_plan.py bug 'Login fails on mobile'")
        sys.exit(1)
    
    plan_type = sys.argv[1]
    
    if plan_type == "feature":
        if len(sys.argv) < 3:
            print("Usage: python create_plan.py feature <title> [features...]")
            sys.exit(1)
        title = sys.argv[2]
        features = sys.argv[3:] if len(sys.argv) > 3 else ["Core feature"]
        goal = f"Implement {title}"
        plan = create_feature_plan(title, goal, features)
        
    elif plan_type == "bug":
        if len(sys.argv) < 3:
            print("Usage: python create_plan.py bug <title>")
            sys.exit(1)
        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else f"Fix {title}"
        plan = create_bug_fix_plan(title, description)
        
    else:
        print(f"Unknown plan type: {plan_type}")
        sys.exit(1)
    
    print(plan.to_markdown())

if __name__ == "__main__":
    main()
