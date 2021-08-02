from jsonupdate_ng import jsonupdate_ng
import json, time

if __name__ == '__main__':
    baseJson = json.load(open('base.json'))
    headJson = json.load(open('head.json'))
    updatedJson = jsonupdate_ng.updateJson(baseJson, headJson)
    print(json.dumps(updatedJson, indent=4))

    exists = jsonupdate_ng.checkIfNodeExistsAtGivenJsonPath(baseJson, "$.data")

