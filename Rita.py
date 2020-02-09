import time
import pafy
import youtube_dl
'''
 REQUIREMENTS
 - Install pafy
 - Install Youtube_dl latest update
'''

def singleAudio():
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



def singleVideo():
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


def playlistVideo():
    playlistlinks= {}
    while(1):
        link = input("Copy and paste the Youtube link: ")
        youtube_dl.YoutubeDL(playlistlinks).download([link])
    




def userpick():
    print('Please pick a program to run')
    time.sleep(3)
    print('1.Single Downlaod\n2.Multi Download')
    singlePickValue = int(input('Enter Value: '))
    print('Loading..')
    time.sleep(2)
    print('Loading............')
    time.sleep(3)
    print('Trying to get to Thanos before he gets to me..........')
    time.sleep(3)
    print('"Dread it Run from it, Destiny arrives all the same, Now its here, or should i say I AM" ')
    
    if singlePickValue == 1:
        print('1.Audio\n2.Video')
        singlePickFinal = int(input('Enter Value:'))

        if singlePickFinal == 1:
            singleAudio()
        elif singlePickFinal == 2:
            singleVideo()    
        
    elif singlePickValue == 2:
        playlistVideo()



userpick()          
