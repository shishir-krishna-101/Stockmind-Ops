import os

docs_dir = r"c:\Users\Demon Slayer\Downloads\Stockmind-Ops\docs"

def write_doc(path, content):
    full_path = os.path.join(docs_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

def tech_template(name, what, problem, usage, status, selected_reason, alts_considered, alts_rejected_reason, tradeoffs, security, operational, cost, reconsider, replacement, alternative_analysis=""):
    return f"""## {name}

### 1. What is it?
{what}

### 2. What problem does it solve?
{problem}

### 3. Where is it used in StockMind?
{usage}

### 4. Is it implemented or planned?
**Status:** {status}

### 5. Why was it selected?
{selected_reason}

### 6. What alternatives were considered?
{alts_considered}

### 7. Why were those alternatives not selected?
{alts_rejected_reason}

### 8. What are the trade-offs?
{tradeoffs}

### 9. What are the security implications?
{security}

### 10. What are the operational implications?
{operational}

### 11. What are the cost implications?
{cost}

### 12. When should we reconsider it?
{reconsider}

### 13. What would replacing it look like?
{replacement}

{alternative_analysis}
"""

def adr_template(num, title, status, context, decision, alts, reasoning, tradeoffs, consequences, reconsider):
    return f"""# ADR-{num}: {title}

**Status:** {status}

## Context
{context}

## Decision
{decision}

## Alternatives Considered
{alts}

## Reasoning
{reasoning}

## Trade-offs
{tradeoffs}

## Consequences
{consequences}

## Future Reconsideration Triggers
{reconsider}
"""

print("Helper functions ready.")
