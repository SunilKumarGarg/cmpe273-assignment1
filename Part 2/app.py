

import sys, re, yaml, json
from github import Github


from flask import Flask

app = Flask(__name__)

#get application argument
link = sys.argv[1]
if len(link) <= 0:
    print "Enter the link"
    exit()

#Get username and repo
outputPattern = re.compile(r'https://github.com/(\S+)/(\S+)')
details = outputPattern.search(str(link)).groups()
r = Github()


@app.route("/v1/<configName>")
def hello(configName):
    try: 
        file = re.compile(r'(\S+)\.(\S+)')
        fileDetails = file.search(str(configName)).groups()

        if 'json' != str.lower(fileDetails[1]) and 'yml' != str.lower(fileDetails[1]):
            return "Only Json and yml format supported"

        config = r.get_user(details[0]).get_repo(details[1]).get_contents(configName).decoded_content

        if 'yml' == str.lower(fileDetails[1]): 
            try:
                yaml.dump(config)
                return config
            except:
                return "File is not in Yml format."
            
        else:   
            try:
                json.dumps(config)
                return config
            except:
                return "File is not in Json format."
    except:
        return "No file found"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')















