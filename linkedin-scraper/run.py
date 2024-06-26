"""
This example run script shows how to run the Linkedin.com scraper defined in ./linkedin.py
It scrapes product data and saves it to ./results/

To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
import asyncio
import json
from pathlib import Path
import linkedin

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    # enable scrapfly cache
    linkedin.BASE_CONFIG["cache"] = False
    linkedin.BASE_CONFIG["debug"] = True

    print("running Linkedin scrape and saving results to ./results directory")

    profile_data = await linkedin.scrape_profile(
        urls=[
            "https://www.linkedin.com/in/williamhgates"
        ]
    )
    with open(output.joinpath("profile.json"), "w", encoding="utf-8") as file:
        json.dump(profile_data, file, indent=2, ensure_ascii=False)    

    company_data = await linkedin.scrape_company(
        urls=[
            "https://linkedin.com/company/microsoft",
            "https://linkedin.com/company/google",
            "https://linkedin.com/company/apple"
        ]
    )
    with open(output.joinpath("company.json"), "w", encoding="utf-8") as file:
        json.dump(company_data, file, indent=2, ensure_ascii=False)    

    job_search_data = await linkedin.scrape_job_search(
        # it include other search parameters, refer to the search pages on browser for more details
        keyword="Python Developer",
        location="United States",
        max_pages=3
    )
    with open(output.joinpath("job_search.json"), "w", encoding="utf-8") as file:
        json.dump(job_search_data, file, indent=2, ensure_ascii=False)    

    job_data = await linkedin.scrape_jobs(
        urls=[
            "https://www.linkedin.com/jobs/view/python-developer-internship-at-mindpal-3703081824",
            "https://www.linkedin.com/jobs/view/python-developer-at-donato-technologies-inc-3861152070",
            "https://www.linkedin.com/jobs/view/python-developer-at-ltimindtree-3846584680"
        ]
    )
    with open(output.joinpath("jobs.json"), "w", encoding="utf-8") as file:
        json.dump(job_data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    asyncio.run(run())
        