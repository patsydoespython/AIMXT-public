from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from AIMXT.llm import LLMTaskOperator, LLMTaskCoordinator
from AIMXT.task import Task

# Example usage
if __name__ == "__main__":
    # Create a task with initial subtasks
    article_task = Task(name="Write Article",
                        description="Write an article about AI advancements. The final output should strictly include only the title and the content, without any additional sections or formatting.")

    tasks = [
        article_task
    ]

    # llm = ChatOllama(model="mistral-nemo:latest", temperature=0)
    # tool_llm = ChatOllama(model="mistral-nemo:latest", format="json", temperature=0)

    llm = ChatOpenAI(
        model_name='gpt-4o-mini'
    )
    # Create specialized agents
    agents = [
        LLMTaskOperator(
            name="research",
            role="Research Analyst",
            context="Extensive knowledge of research methodologies,"
                    " data collection techniques, and analytical tools. "
                    "Proficient in both qualitative and quantitative research methods. "
                    "Familiar with academic, market, and industry-specific research practices.",
            skills=[
                "Market Research",
                "Data Analysis",
                "Literature Review",
                "Survey Design",
                "Interviewing Techniques",
                "Statistical Analysis",
                "Trend Forecasting",
                "Competitive Intelligence",
                "Research Report Writing",
                "Data Visualization"
            ],
            llm=llm
        ),

        LLMTaskOperator(
            name="writing",
            role="Content Strategist & Writer",
            context="Deep understanding of various writing styles, content formats, "
                    "and audience engagement strategies. Knowledgeable about "
                    "SEO-friendly writing, storytelling techniques, and brand voice "
                    "development. Familiar with content management systems and digital publishing platforms.",
            skills=[
                "Creative Writing",
                "Technical Writing",
                "Copywriting",
                "Content Strategy",
                "Storytelling",
                "SEO Writing",
                "Editing and Proofreading",
                "Brand Voice Development",
                "Audience Analysis",
                "Multimedia Content Creation"
            ],
            llm=llm
        ),

        LLMTaskOperator(
            name="seo_optimization",
            role="SEO Strategist",
            context="Comprehensive understanding of search engine algorithms,"
                    " ranking factors, and SEO best practices. Proficient in technical SEO,"
                    " content optimization, and link building strategies. Familiar with local SEO,"
                    " mobile optimization, and voice search optimization.",
            skills=[
                "Keyword Research",
                "On-Page SEO",
                "Off-Page SEO",
                "Technical SEO",
                "Content Optimization",
                "Link Building",
                "Local SEO",
                "Mobile SEO",
                "Voice Search Optimization",
                "SEO Analytics and Reporting"
            ],
            llm=llm
        ),

        LLMTaskOperator(
            name="web_publishing",
            role="Digital Content Manager",
            context="Extensive knowledge of web publishing platforms, "
                    "content management systems, and digital asset management. "
                    "Proficient in HTML, CSS, and basic JavaScript. Familiar with web accessibility standards, "
                    "responsive design principles, and UX/UI best practices.",
            skills=[
                "CMS Management",
                "HTML/CSS",
                "Content Scheduling",
                "Digital Asset Management",
                "Web Accessibility",
                "Responsive Design",
                "Version Control",
                "A/B Testing",
                "Web Analytics",
                "User Experience Optimization"
            ],
            llm=llm
        )
    ]

    task_manager = LLMTaskCoordinator(tasks, agents, llm=llm)
    tasks = task_manager.do(inputs=b"")

    for t in tasks:
        print(t.final_answer)
