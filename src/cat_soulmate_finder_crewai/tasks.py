"""Tasks."""
from crewai import Task
from textwrap import dedent
from cat_soulmate_finder_crewai.agents import research_Agent, writer_Agent, editor_Agent
from cat_soulmate_finder_crewai.tools import WikipediaSearchTool, WebSearchTool

# price_researcher_task = Task(description=dedent("""
#     Reseach the price range of the given cat breed by 
#     using your research tools.
#     """),
#     expected_output=dedent("""
#     Give the price range from the lower to the upper quartile 
#     of the cat breed as well as the mean price.
#     """),
        
#     agent=research_Agent,   # assign one agent for the task
#     tools=[WikipediaSearchTool(), WebSearchTool()] # assign tools to the task which can be used to answer it. Can be done in the agents instead
# )

cat_internet_research_task = Task(description=dedent("""
    Using your research tools, research the internet for a wide variety of many
    cat breeds (at least 20), even lesser known breeds like Nebelung, for traits and features about each. 
    These informations must help to decide, if the cat breed is a good fit living with a human depending on their life style, living situation and character. 
    Should contain things like size, color and character traits of the cat. 
    Only list information you are certian of, do not make things up.
    """),
    expected_output=dedent("""
    List the information in JSON format.
    It must contain the following attributes:
    - Average height and length of the cat
    - Average weight of the cat
    - Average lifespan of the cat
    - Average price of the cat
    - If the cat can live with other pets
    - If the cat must go outside or can live only inside
    - how allergenic the cat is
    - how much attention the cat needs and if it is fine if the humans are away for their job all day
    but you are free to add more information if it could help decide later, if the cat can fit to the living style of a human.
    """),
    agent=research_Agent,
    tools=[WikipediaSearchTool(), WebSearchTool()]
)

cat_human_comparison_task = Task(description=dedent("""
    find the best 5 cat breeds that fit to the human 
    personality and life style: {human_input}.
    Dont make up information about the human, choose the most compatiple cats only based on the information you are given.
    You can add preferences of the cats regarding to the owner to the answer about things you dont know about the human.
    """),
    expected_output=dedent("""
    List the 5 cat breeds that fit to the human personality
    """),
    agent=research_Agent,
    #tools=[WikipediaSearchTool(), WebSearchTool()]
)

# cat_image_retival_task = Task(description=dedent("""
#     find images of the cat breeds that are selected.
#     """),
#     agent=agent
# )

generate_report_task = Task(description=dedent("""
    generate a report that contains all the 
    information about the selected cats and 
    why it fits together perfectly the the user.
    """), 
    expected_output=dedent("""
    List the gathered information of the 5 cat breeds that fit the best to the 
    humans living situation and personality.
    Give for each cat bullet points about information of the cat breed like: 
    - Average size of the cat (in cm),
    - Average weight of the cat (in kg),
    - Average lifespan of the cat (in years),
    - Average price of the cat (in Euro)
    - If the cat can live with other pets.
    You can add more bullet points if you see fit, like if they are good with other pets or kids, 
    if its adds value for the description of the person. 
    Add a short summary of about 3 to 4 sentences for each cat, why it is a good fit to live with the person.
    """),
    agent=writer_Agent
)

quality_control_task = Task(description=dedent("""
    Check the report for spellings and grammartical mistakes and improve the general quality of writing, 
    if you see issues. Don't change facts or the meaning of text. You can display it in a better way, 
    if you think it delivers the meaning better for the reader, but do not change the structure to much. 
    But you should remove bullet points if they are empty.
    """), 
    expected_output=dedent("""
    List the gathered information of the cat breeds in bullet points and below a concise summary 
    of why the cat breeds fit to the human personality and living style.
    """),
    agent=editor_Agent
)
