import requests
import re
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser") # pass page.content cos its better than page.text
results = soup.find(id="ResultsContainer")  # gives the entire div

#print(results.prettify()) # 

job_elements = results.find_all("div", class_="card-content") # find all card_content

#for job_element in job_elements:  # iterate through everthing
    #print(job_element, end="\n"*2)

"""for job_element in job_elements:
    title_element = job_element.find("h2", class_="title") #it gonna print something like ; ,<h2> </h2>
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()"""

"""for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip()) #.text to extract actual text i.e DevOps
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()"""

#python_jobs = results.find_all("h2", string="Python") #gonna search for exactly 'Python'
#print(python_jobs) # []

python_jobs = results.find_all( # you can pass a fucntion
    "h2", string=lambda text: "python" in text.lower()
)


"""regex_pattern = r'[Pp]ython' #regex also worked
python_jobs = results.find_all(
    "h2", string=lambda text: re.findall(regex_pattern,text) #"python" in text.lower()
)
print(python_jobs)
print(len(python_jobs))"""

"""for job_element in python_jobs:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip()) #.text to extract actual text i.e DevOps
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    #Terminal:
        #print(title_element.text.strip()) #.text to extract actual text i.e DevOps
#AttributeError: 'NoneType' object has no attribute 'text'
    """

#for py_job in python_jobs:
    #print(py_job.text.strip())

"""python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)"""


"""<div class="card">
  <div class="card-content"> #parent 3
    <div class="media"> #parent 2
      <div class="media-left">
        <figure class="image is-48x48">
          <img
            src="https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg"
            alt="Real Python Logo"
          />
        </figure>
      </div>
      <div class="media-content"> #parent 1
        <h2 class="title is-5">Senior Python Developer</h2>
        <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
      </div>
    </div>

    <div class="content">
      <p class="location">Stewartbury, AA</p>
      <p class="is-small has-text-grey">
        <time datetime="2021-04-08">2021-04-08</time>
      </p>
    </div>
    <footer class="card-footer">
      <a
        href="https://www.realpython.com"
        target="_blank"
        class="card-footer-item"
        >Learn</a
      >
      <a
        href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
        target="_blank"
        class="card-footer-item"
        >Apply</a
      >
    </footer>
  </div>
</div>
"""

# <div class="card-content"> #parent 3
# <div class="media"> #parent 2
#<div class="media-content"> #parent 1
# Logic is to get other info like 'company','location' .
#     We need to get a parent that enclose everything we need which is "card-content"
#           count number of indentations to that parent...Viola.
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs # 3 parents indicates 3 generations ish
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip()) #.text to extract actual text i.e DevOps
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

"""for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())
    #If you run this code snippet, 
    # then you’ll get the link texts 'Learn' and 'Apply' instead of the associated URLs.
    """

"""for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

    #since we are looking for the apply link
    # the apply link is the second <a> tag i.e first is for learn

        """

for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")




