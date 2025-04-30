#Importing tools
import json
import requests

#Opening text file to append insight data
myText = open("MetricsData.txt","w")

#Loading insight "data" into variable. Its a json list of insights from ICS
url = "https://asb.customer.divvycloud.com/v2/public/insights/list?detail=false&pack_ids=backoffice:36"
headers = { 'Api-Key': 'xnG_q6EmNRQ6xF3_MlFxs6MJ2DEHH1dcV9O1WdUV8mPiZE_MssM' }
response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

#Loading "clouds" into variable. Note: not needed anymore. Previously used for filtering only AWS cloud type.
url = "https://asb.customer.divvycloud.com/v2/public/clouds/list"
response = requests.request("GET", url, headers=headers)
clouds = json.loads(response.text)

#initializing severety count
critical,high,medium,low = 0,0,0,0

###########################################################################
#Function Categorizing Severity                                           #
###########################################################################
def severityFilter(severity, customSeverity):
    global critical,high,medium,low
    if (customSeverity == None):
        match severity:
            case 5: critical+=1
            case 4: high+=1
            case 3: medium+=1
            case 2: low+=1
    elif(customSeverity >= 2):
        match customSeverity:
            case 5: critical+=1
            case 4: high+=1
            case 3: medium+=1
            case 2: low+=1
###########################################################################
#                                                                         #
###########################################################################


###########################################################################
#Running Both Functions and Returning Values                              #
###########################################################################
print(type(data))
for i in range(0, len(data)):   
    if (data[i]['results'] >= 1): #and cloudFilter(data[i]['by_cloud'])  This piece of code could be added to filter for AWS clouds
        severityFilter(data[i]['severity'], data[i]['custom_severity']) 
###########################################################################
#Running Both Functions and Returning Values                              #
###########################################################################



###########################################################################
#Function Filtering AWS Clouds. NOT USED ANYMORE                          #
###########################################################################
#def cloudFilter(insightClouds):
#    global clouds
#    for i in insightClouds:
#        if(insightClouds[i]['count'] >= 1):
#            for x in clouds['clouds']:
#               if (str(x['id']) == i and "AWS" in x['cloud_type_id']):
#                    return True
#    return False
###########################################################################
#                                                                         #
###########################################################################

print("\n\n\t")
print("Insight Data:")
print("Critical:",critical)
print("High:",high)
print("Medium:",medium)
print("Low:", low, "\n")

#Writing data to text file
#myText.write("Insight Data:\n")
#myText.write(f"Critical: {str(critical)}\n")
#yText.write(f"High: {str(high)}\n")
#myText.write(f"Medium: {str(medium)}\n")
#yText.write(f"Low: {str(low)}\n")