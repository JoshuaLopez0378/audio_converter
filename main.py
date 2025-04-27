from os import path
from pydub import AudioSegment

root_path = "E:/Games/x64/soundlines"
to_convert_path = str(
    input("Convert, enter folder: ")
)  # e.g "E:/Games/x64/soundlines/chimaerajakiro/"
dialogues_folder = {
    "yes": "Yes",
    "yesattack": "Attack",
    "ready": "Ready",
    "pissed": "Pissed",
    "what": "What",
}  # e.g "E:/Games/x64/soundlines/chimaerajakiro/yes/"


def convert_mp3_to_wav_mono(input_folder, output_folder, d_folder):
    sound = AudioSegment.from_mp3(input_folder)
    # sound.export(output, format="wav")
    sound = sound.set_channels(1)
    sound.export(output_folder + ".wav", format="wav")
    return "OK"


input_folder = root_path + to_convert_path
output_folder = "./" + to_convert_path
convert_mp3_to_wav_mono(input_folder, output_folder, dialogues_folder)
