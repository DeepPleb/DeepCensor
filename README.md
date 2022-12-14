# DeepCensor
## Censor swear words automatically using Speech-to-Text.

Here's a [demo](http://sndup.net/q924) (Contains profane language!)

Using profane language can land you in trouble. But with the help of AI, we can censor swear words automatically. DeepCensor is a piece of python code that can mute swear words in any audio/video file **automatically**.

## Use Cases
* **Youtube videos**: A video containing too many swear words can get it demonetized. With DeepCensor a creator can make sure this doesn't happen. 
* **Explicit music**: You can make a radio version of an explicit version especially using the `video` model that [DeepGram](https://developers.deepgram.com/documentation/features/model/) provides.
* **Live News**: Sometimes live news might contain swears. Profane language can easily be censored using the [live transcription](https://developers.deepgram.com/documentation/getting-started/streaming/) feature.


## Requirements:
* Deepgram Python SDK [https://deepgram.com/]
* ffmpeg [https://ffmpeg.org/]

## Usage
Install Deepgram Python SDK:

`pip install deepgram-sdk`



Install ffmpeg:

`pip install ffmpeg-python`



Run script.py. Make sure you've added the correct .wav audio file path:

`python script.py`

---
After you run the script you should see a .wav file called 'out.wav' in your folder
