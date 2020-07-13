from pathlib import Path
import requests
filename = Path('DAA.pdf')
url = 'https://www.tutorialspoint.com/design_and_analysis_of_algorithms/design_and_analysis_of_algorithms_tutorial.pdf'
response = requests.get(url)
filename.write_bytes(response.content)
