import requests

url = "https://google.com"

answer = requests.get(url)

print(dir(answer))

counter = 0

if (answer):
    while (counter<=100):
        print(answer)
        counter=counter+1
        if (counter>80 and counter < 100):
            print(counter,"ja falta pouco pah")
        if (counter==100):
            print(counter,"ja acabou finalmente")
