from os import path, listdir, mkdir, rename, makedirs
from pydub import AudioSegment
import json
import threading


root_dir = "E:/Games/war3mpqeditor/soundlines/"
sfx_root_dir = root_dir + "others/"
# to_convert_dir = str(
# input("Convert, enter dir: ")
# )  # e.g "E:/Games/x64/soundlines/chimaerajakiro/"

# base_char_name = str(input("Enter base char name: "))
# input_dir = root_dir + to_convert_dir

# dialogues_dir = ["yes", "yes attack", "ready", "pissed", "what"]

with open("dir_mapping.json", "r") as dir_mapping:
    sfx_json = json.load(dir_mapping)


def convert_mp3_to_wav_mono(input_dir, d_dir, base_char_name):
    print("Input dir: ", input_dir)
    print("Converting...")
    try:
        mkdir("out_results/" + base_char_name)
    except:
        print("exists")
    for dir in d_dir:
        split_f = dir.split(" ")
        print(len(split_f))
        id_f = 1
        try:
            d_sub_dir = listdir(input_dir + "/" + dir)
            print("Current dir: ", dir)
            print("Input Files List:", d_sub_dir)
            print()
            for file in d_sub_dir:
                if len(split_f) > 1:
                    dir_new = split_f[0].capitalize() + split_f[1].capitalize()
                else:
                    dir_new = dir.capitalize()
                sound = AudioSegment.from_mp3(input_dir + "/" + dir + "/" + file)
                sound = sound.set_channels(1)
                sound.export(
                    "out_results/"
                    + f"{base_char_name}/"
                    + base_char_name
                    + dir_new
                    + str(id_f)
                    + ".wav",
                    format="wav",
                )

                print("Output To: ", base_char_name + input_dir + str(id_f) + ".wav")
                id_f += 1
        except:
            continue
    return "OK"


# convert_mp3_to_wav_mono(input_dir, dialogues_dir, base_char_name)
# def rename_to_mp3(file_dir):
#     return rename(file_dir)


def convert_spells_weapons_sfx(sfx, sfx_root_dir_inp):

    for sfx_dir, value in sfx.items():
        print(f"out_results/{value['audio_mod_dir'][0]}/")
        print("MAKING DIR")
        try:
            makedirs(f"out_results/{value['audio_mod_dir'][0]}/")
        except:
            print("exists")
        if "_" in sfx_dir:
            sfx_dir_subpath = "spells/"
        else:
            sfx_dir_subpath = "weapons/"

        # input dir
        input_dir_mod = sfx_root_dir_inp + sfx_dir_subpath + sfx_dir
        print(f"INPUT DIR: {input_dir_mod}")

        # input dir files
        input_dir_files = listdir(input_dir_mod)

        print(f"SFX VALUE {value['files']} \nSFX VALUE FILES LEN {len(value['files'])}")
        print(
            f"SFX VALUE {value['file_mod_name']} \nSFX VALUE LEN {len(value['file_mod_name'])}"
        )

        if len(value["files"]) > 1 and len(value["file_mod_name"]) == 1:
            print("MERGING AND CONVERTING")

            try:
                for cur_sfx in value["files"]:
                    original_file_dir = f"{input_dir_mod}/{cur_sfx}"
                    print("ORIGINAL: ", original_file_dir)
                    renamed_file_dir = f"{original_file_dir.split('.')[0]}.mp3"
                    print("RENAMED:", renamed_file_dir)
                    rename(original_file_dir, f"{renamed_file_dir}")
            except:
                pass
            cur_sfx_init_list = ""
            # for cur_sfx_renamed in input_dir_mod:
            # cur_sfx_init_list += cur_sfx_renamed
            print(cur_sfx_init_list)
            a1 = f"{input_dir_mod}/{listdir(input_dir_mod)[0]}"
            a2 = f"{input_dir_mod}/{listdir(input_dir_mod)[1]}"
            sound = AudioSegment.from_mp3(a1)
            soundb = AudioSegment.from_mp3(a2)
            combined = sound.overlay(soundb)
            combined = combined.set_channels(1)
            combined.export(
                f"out_results/{value['audio_mod_dir'][0]}/{value['file_mod_name'][0]}",
                format="wav",
            )

        elif len(value["files"]) > 1 and len(value["file_mod_name"]) > 1:
            print("CONVERTING SUBDIR")

            # input subdir files
            for inc, cur_dir in enumerate(input_dir_files):

                # if "." in cur_dir and :

                if "." not in cur_dir:
                    cur_dir_sfx = f"{input_dir_mod}/{cur_dir}"
                    print(f"CURRENT DIR: {cur_dir_sfx}")
                    print(f"CURRENT FILES: {listdir(cur_dir_sfx)}")
                    try:
                        original_file_dir = f"{cur_dir_sfx}/{value['files'][inc]}"
                        print("ORIGINAL: ", original_file_dir)
                        renamed_file_dir = f"{original_file_dir.split('.')[0]}.mp3"
                        print("RENAMED:", renamed_file_dir)
                        rename(original_file_dir, f"{renamed_file_dir}")
                    except:
                        pass
                    sound = AudioSegment.from_mp3(
                        f"{cur_dir_sfx}/{value['files'][inc].split('.')[0]}.mp3"
                    )
                    sound = sound.set_channels(1)
                    sound.export(
                        f"out_results/{value['audio_mod_dir'][0]}/{value['file_mod_name'][inc]}",
                        format="wav",
                    )
        else:
            print("CONVERTING IMMEDIATELY")

            try:
                original_file_dir = f"{input_dir_mod}/{value['files'][0]}"
                print("ORIGINAL: ", original_file_dir)
                renamed_file_dir = f"{original_file_dir.split('.')[0]}.mp3"
                print("RENAMED:", renamed_file_dir)
                rename(original_file_dir, f"{renamed_file_dir}")
            except:
                pass
            sound = AudioSegment.from_mp3(renamed_file_dir)
            sound = sound.set_channels(1)
            sound.export(
                f"out_results/{value['audio_mod_dir'][0]}/{value['file_mod_name'][0]}",
                format="wav",
            )

        print(" ============== ")


convert_spells_weapons_sfx(sfx_json, sfx_root_dir)
