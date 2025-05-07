import os
import subprocess as sp
import stt_functions as stt

file_dir = os.path.abspath(os.path.dirname(__file__))
stt_dir = f"{file_dir}/stt_data"

def solve_lis_grab_img(cat_division, exposure_time_ms):
    exptime_micros = 1000 * exposure_time_ms
    image_dir = f"{stt_dir}/stt_img.jpg"
    print(f"\n---> STT: Taking picture with {exposure_time_ms} ms of exposure time.\n")
    task = f"libcamera-still -o {image_dir} -t 1 --width 1024 --height 1024 --shutter {exptime_micros}"
    process = sp.Popen(task, shell=True, stdout=sp.PIPE)
    process.wait()
    if process.returncode != 0:
        raise OSError("---> ERROR: Camera capture failed!")
    stt.solve_lis(image_dir, cat_division, stt_dir)

def solve_lis_sample_rpi(cat_division, n_pic):
    if n_pic < 1 or n_pic > 50:
        raise ValueError("---> ERROR: --npic must be between 1 and 50")
    print(f"\n---> STT: Analyzing Sample_images/RPi/img_{n_pic}.jpg using catalog division {cat_division}\n")
    image_dir = f"{file_dir}/Sample_images/RPi/img_{n_pic}.jpg"
    stt.solve_lis(image_dir, cat_division, stt_dir)

def solve_lis_sample_stereo(cat_division, n_pic):
    stereo_images_list = sorted([f for f in os.listdir(f"{file_dir}/Sample_images/STEREO") if f.endswith(".fts")])
    if n_pic < 1 or n_pic > len(stereo_images_list):
        raise ValueError(f"---> ERROR: --npic must be between 1 and {len(stereo_images_list)}")
    image_name = stereo_images_list[n_pic - 1]
    print(f"\n---> STT: Analyzing Sample_images/STEREO/{image_name} using catalog division {cat_division}\n")
    image_dir = f"{file_dir}/Sample_images/STEREO/{image_name}"
    stt.solve_lis(image_dir, cat_division, stt_dir, lis_type="stereo")
def solve_lis_custom(cat_division, image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"---> ERROR: The file {image_path} does not exist.")
    print(f"\n---> STT: Analyzing custom image {image_path} using catalog division {cat_division}\n")
    stt.solve_lis(image_path, cat_division, stt_dir, lis_type="stereo")
