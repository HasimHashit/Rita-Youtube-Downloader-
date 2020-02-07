import pafy

def audio():
    ##pafy for getting url==> audio
    #url of the video
    url = input('Enter your url: ')

    #calling the new method of pafy
    result = pafy.new(url)

    #getting the best audio from the reuslt using getbest()
    best_quality_audio = result.getbestaudio()
    #printing to see the quality
    print(best_quality_audio)

    #downlaoding it using the download()
    best_quality_audio.download()



def video():
    ##pafy for getting url==> video
    ##url of the video
    url = input('Enter your url: ')
    #calling the new method of pafy
    result = pafy.new(url)
    #getting the best quality of video from the reult 
    best_quality_audio = result.getbest()
    #printing the quality of the video
    print(best_quality_audio)
    #downloading the video
    best_quality_audio.download()


def userpick():
    userinput = eval(input('Enter you pick 1.audio 2.video: '))
    if userinput == 1:
        audio()
    elif userinput == 2:
        video()  
    else:
        print('pls pick a valid number')    



userpick()          