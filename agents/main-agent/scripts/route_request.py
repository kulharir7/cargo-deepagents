#!/usr/bin/env python3
\"\"\"Request routing utility for Main Agent.

Analyzes user requests and determines which specialist agent to route to.
\"\"\"

import re
import sys
from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum

class Agent(Enum):
    MAIN = "main-agent"
    BASE = "base-agent"
    CODER = "coder-agent"
    PLANNER = "planner-agent"

@dataclass
class RoutingResult:
    \"\"\"Result of routing analysis.\"\"\"
    agent: Agent
    confidence: float
    keywords_matched: List[str]
    reason: str
    multi_agent: bool = False
    agent_sequence: List[Agent] = None

# Keyword patterns for each agent
AGENT_PATTERNS = {
    Agent.BASE: {
        "file_ops": ["read", "write", "edit", "create", "delete", "list", "ls", "cat"],
        "shell": ["run", "execute", "command", "shell", "terminal"],
        "web": ["search", "find", "browse", "fetch", "url", "web"],
    },
    Agent.CODER: {
        "code_gen": ["write code", "implement", "create function", "create class", "build"],
        "debug": ["fix", "bug", "debug", "error", "exception", "issue"],
        "refactor": ["refactor", "clean", "optimize", "improve", "simplify"],
        "test": ["test", "unit test", "integration test", "coverage"],
    },
    Agent.PLANNER: {
        "planning": ["plan", "roadmap", "steps", "phases", "milestone"],
        "estimation": ["estimate", "how long", "timeline", "duration"],
        "breakdown": ["break down", "decompose", "analyze structure"],
    }
}

MULTI_INDICATORS = ["and", "then", "after that", "first", "second", "also", "additionally"]

def extract_actions(text: str) -> List[str]:
    \"\"\"Extract action verbs from text.\"\"\"
    action_verbs = [
        "read", "write", "edit", "create", "delete", "list", "run", "execute",
        "search", "find", "browse", "implement", "build", "fix", "debug",
        "refactor", "optimize", "test", "plan", "estimate", "analyze"
    ]
    
    found = []
    text_lower = text.lower()
    for verb in action_verbs:
        if verb in text_lower:
            found.append(verb)
    return found

def calculate_score(text: str, agent: Agent) -> Tuple[float, List[str]]:
    \"\"\"Calculate matching score for an agent.\"\"\"
    text_lower = text.lower()
    score = 0
    matched = []
    
    if agent not in AGENT_PATTERNS:
        return 0, []
    
    for category, keywords in AGENT_PATTERNS[agent].items():
        for keyword in keywords:
            if keyword in text_lower:
                score += 1
                matched.append(keyword)
    
    return score, matched

def detect_multi_agent(text: str) -> bool:
    \"\"\"Detect if request needs multiple agents.\"\"\"
    text_lower = text.lower()
    
    # Check for multi-agent indicators
    for indicator in MULTI_INDICATORS:
        if indicator in text_lower:
            return True
    
    # Check for multiple action types
    actions = extract_actions(text)
    
    # If multiple different action categories
    base_actions = ["read", "write", "edit", "create", "list", "run", "search"]
    coder_actions = ["implement", "build", "fix", "debug", "refactor", "test"]
    planner_actions = ["plan", "estimate", "analyze"]
    
    has_base = any(a in base_actions for a in actions)
    has_coder = any(a in coder_actions for a in actions)
    has_planner = any(a in planner_actions for a in actions)
    
    return sum([has_base, has_coder, has_planner]) > 1

def route_request(text: str) -> RoutingResult:
    \"\"\"Route request to appropriate agent.\"\"\"
    
    # Check if multi-agent
    is_multi = detect_multi_agent(text)
    
    # Calculate scores for each agent
    scores = {}
    matched = {}
    
    for agent in [Agent.BASE, Agent.CODER, Agent.PLANNER]:
        score, keywords = calculate_score(text, agent)
        scores[agent] = score
        matched[agent] = keywords
    
    # Find best match
    best_agent = max(scores, key=scores.get)
    best_score = scores[best_agent]
    
    # Normalize confidence (0-100%)
    total_keywords = sum(scores.values())
    if total_keywords > 0:
        confidence = (best_score / total_keywords) * 100
    else:
        confidence = 0
        best_agent = Agent.MAIN
    
    # Build reason
    if best_agent == Agent.MAIN:
        reason = "No specific agent matched - handling directly"
    else:
        reason = f"Matched {', '.join(matched[best_agent])} keywords"
    
    # Handle multi-agent scenario
    agent_sequence = None
    if is_multi and confidence > 40:
        # Build sequence based on action order
        agent_sequence = []
        actions = extract_actions(text)
        for action in actions:
            if action in ["read", "write", "edit", "list", "run", "search"]:
                if Agent.BASE not in agent_sequence:
                    agent_sequence.append(Agent.BASE)
            elif action in ["implement", "build", "fix", "debug", "refactor", "test"]:
                if Agent.CODER not in agent_sequence:
                    agent_sequence.append(Agent.CODER)
            elif action in ["plan", "estimate"]:
                if Agent.PLANNER not in agent_sequence:
                    agent_sequence.append(Agent.PLANNER)
    
    return RoutingResult(
        agent=best_agent,
        confidence=confidence,
        keywords_matched=matched[best_agent],
        reason=reason,
        multi_agent=is_multi and len(agent_sequence) > 1 if agent_sequence else False,
        agent_sequence=agent_sequence
    )

def format_result(result: RoutingResult) -> str:
    \"\"\"Format routing result as readable text.\"\"\"
    lines = [
        f"Agent: {result.agent.value}",
        f"Confidence: {result.confidence:.0f}%",
        f"Matched: {', '.join(result.keywords_matched) if result.keywords_matched else 'None'}",
        f"Reason: {result.reason}",
    ]
    
    if result.multi_agent and result.agent_sequence:
        sequence = " → ".join([a.value for a in result.agent_sequence])
        lines.append(f"Multi-Agent: Yes")
        lines.append(f"Sequence: {sequence}")
    
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python route_request.py \"your request\"")
        print()
        print("Examples:")
        print("  python route_request.py \"read the file config.yaml\"")
        print("  python route_request.py \"write a function to validate email\"")
        print("  python route_request.py \"create a plan for building an API\"")
        sys.exit(1)
    
    request = " ".join(sys.argv[1:])
    result = route_request(request)
    
    print("=" * 50)
    print("ROUTING RESULT")
    print("=" * 50)
    print(format_result(result))
    print("=" * 50)

if __name__ == "__main__":
    main()
