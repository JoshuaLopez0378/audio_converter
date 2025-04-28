from os import path, listdir, mkdir
from pydub import AudioSegment
import threading

root_path = "E:/Games/x64/soundlines/"
to_convert_path = str(
    input("Convert, enter folder: ")
)  # e.g "E:/Games/x64/soundlines/chimaerajakiro/"
base_char_name = str(input("Enter base char name: "))
dialogues_folder = [
    "yes",
    "yes attack",
    "ready",
    "pissed",
    "what",
]  # e.g "E:/Games/x64/soundlines/chimaerajakiro/yes/"


def convert_mp3_to_wav_mono(input_folder, output_folder, d_folder, base_char_name):
    print("Input Folder: ", input_folder)
    print("Converting...")
    try:
        mkdir("out_results/" + base_char_name)
    except:
        print("exists")
    for folder in d_folder:
        split_f = folder.split(" ")
        print(len(split_f))
        id_f = 1
        try:
            d_sub_folder = listdir(input_folder + "/" + folder)
            print("Current Folder: ", folder)
            print("Input Files List:", d_sub_folder)
            print()
            for file in d_sub_folder:
                if len(split_f) > 1:
                    folder_new = split_f[0].capitalize() + split_f[1].capitalize()
                else:
                    folder_new = folder.capitalize()
                sound = AudioSegment.from_mp3(input_folder + "/" + folder + "/" + file)
                sound = sound.set_channels(1)
                sound.export(
                    "out_results/"
                    + f"{base_char_name}/"
                    + base_char_name
                    + folder_new
                    + str(id_f)
                    + ".wav",
                    format="wav",
                )

                print("Output To: ", base_char_name + input_folder + str(id_f) + ".wav")
                id_f += 1
        except:
            continue
    return "OK"


input_folder = root_path + to_convert_path
output_folder = "./out_results/" + to_convert_path
convert_mp3_to_wav_mono(input_folder, output_folder, dialogues_folder, base_char_name)
