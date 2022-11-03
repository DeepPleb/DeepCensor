import os
from deepgram import Deepgram
import asyncio, json
import sys

# Your Deepgram API Key
DEEPGRAM_API_KEY = '#######################'

# Location of the file you want to transcribe. Should include filename and extension.
# Example of a local file: ../../Audio/life-moves-pretty-fast.wav
# Example of a remote file: https://static.deepgram.com/examples/interview_speech-analytics.wav
FILE = "Your File Path"

# Mimetype for the file you want to transcribe
# Include this line only if transcribing a local file
# Example: audio/wav
MIMETYPE = 'audio/wav'

async def main():

  # Initialize the Deepgram SDK
  deepgram = Deepgram(DEEPGRAM_API_KEY)

  # Check whether requested file is local or remote, and prepare source
  if FILE.startswith('http'):
    # file is remote
    # Set the source
    source = {
      'url': FILE
    }
  else:
    # file is local
    # Open the audio file
    audio = open(FILE, 'rb')

    # Set the source
    source = {
      'buffer': audio,
      'mimetype': MIMETYPE
    }
  
  # Send the audio to Deepgram and get the response
  response = await asyncio.create_task(
    deepgram.transcription.prerecorded(
      source,
      {
        'punctuate': True, 'tier' : 'enhanced'
              }
    )
  )
  transcipt = response["results"]["channels"][0]['alternatives'][0]['words']

  #list of Swears
  swears=['fuck','shit','ass','bitch','whore','dick','fuk']
  ts = []

  #Finding swear words in the transcript
  for j in transcipt:
    for key in swears:
      if key in j['word']:
        se = [j['start'], j['end']]
        ts.extend(se)
  #ts contains the timestamps of all the swear words

  #---Using FFMPEG to mute swears in the audio---

  # ffmpeg -i {0} -c:v copy -af "volume=0:enable=between(t,4,5) volume=0:enable=between(t,8,10)" is the command 
  # used to mute audio between 4s & 5s and 8s & 10s
 
  single_ts = []
  for i in range(0,len(ts),2):
    single_ts.append('between(t,{0},{1})'.format(ts[i],ts[i+1]))

  vol1=''
  for j in single_ts:
      vol1 = vol1 + "volume=enable="+ "'" + j + "'" + ':volume=0' + ","

  vol1 = vol1[:-1]
  vol1 = '''"''' + vol1 + '''"''' 

  #Get the final output audio file 
  final = 'ffmpeg -i {0} -c:v copy -af {1} out.wav'.format(FILE, vol1)
  print(final)
  os.system(final)

try:
  # If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
  #await main()
  asyncio.run(main())
except Exception as e:
  exception_type, exception_object, exception_traceback = sys.exc_info()
  line_number = exception_traceback.tb_lineno
  print(f'line {line_number}: {exception_type} - {e}')
