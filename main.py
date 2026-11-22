import os
from pathlib import Path

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    plan = (
        "Day 1: find 100 local businesses paying for Google Ads but with no landing page. "
        "Email 10/day offering a $49 AI-built landing page + SEO audit, delivered in 2 hours, "
        "paid via Stripe. Close 4 in 30 days = $196. Spend $50 on ads to the same offer. Target $300."
    )
    
    (out_path / "entry.txt").write_text(plan, encoding="utf-8")

if __name__ == "__main__":
    main()
