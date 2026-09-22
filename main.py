# from src.tools.tools import web_search, scrape_url

# result = web_search.invoke({
#     "query": "latest advancements in AI technology"
# })

# print(result)

# result = scrape_url("https://innowise.com/blog/ai-trends")

# print(result)


from src.pipelines.pipelines import run_research_pipeline

topic = "the impact of artificial intelligence on the job market in 2026"

run_research_pipeline(topic)