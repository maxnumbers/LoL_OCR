import pytesseract
import cv2 as cv
import pandas as pd
from time import time

from lol_ocr.helpers.lol_cfg_parser import parse_lol_cfg

# from lol_ocr.helpers.img_transforms import
# from lol_ocr.helpers.predefined_dicts import
# from lol_ocr.ocr_regions.scoreboard_regions import

# Define tesseract path & config settings
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"
TESSDATA_PREFIX = r"C:/Program Files/Tesseract-OCR/"


def time_elapsed():
    """ "returns the amount of time elapsed since module start]"

    Returns:
        [str]: [{minute_count} mins, {second_count} seconds ]
    """
    raw_time = time() - START_TIME
    minute = int(raw_time // 60)
    seconds = int(raw_time % 60)
    elapsed_str = f"{minute} mins, {seconds} sec"

    return elapsed_str


# Class: Process all VOD frames, unless single frame is specified
class RealmParse(object):
    def __init__(
        self,
        input_region,
        vod_path,
        output_path,
        pref_output_format="CSV",
        VOD_frame_number=None,
        lol_cfg_path=None,
        input_subregion=None,
    ):

        # Initialize static vars
        START_TIME = time()
        self.VOD_PATH = VOD_PATH
        self.OUT_PATH = output_path

        # fetch pre-formatted empty dict by region
        self.output_dict = eval("{input_region}_dict")

        # Determine LoL configuration file, if it exists
        if lol_cfg_path:
            self.lol_cfg = parse_lol_cfg(lol_cfg_path)

        # try to open VOD, error if it's not there
        try:
            VOD = cv.VideoCapture(vod_path)

        except:
            AssertionError = True
            print(
                "No video found at designated file path, or couldn't open due to file extension"
            )
            pass

        # perform operations only while VOD is open
        while VOD.IsOpened():

            # determine properties of VOD
            VOD_properties = __get_VOD_props(self, VOD)

            # if we want a specific frame, replace frame index with that frame number
            if VOD_frame_number:
                VOD_properties["FRAME_INDEX"] = int(VOD_frame_number)

            # iteratively process frames (still works even for one frame)
            for frame_number in VOD_properties["FRAME_INDEX"]:

                # see if desired frame exists & can be parsed
                try:
                    # set display to desired frame
                    VOD.set(1, frame_number)
                    # determine whether frame can be successfully read
                    success, current_frame = VOD.read()

                    if success:
                        # if successful, print percent completed and run time
                        ocr_status_update(frame_number, VOD_properties)
                except:
                    if not success:
                        print("Frame #{frame_number} doesn't seem to exist...")
                        break
                    else:
                        print(
                            "Frame was successfully read, but some other error ocurred"
                        )
                        break

                    # check whether frame is in game or not by looking for scoreboard

                    # crop to regions of interest

                # determine whether current frame is in game
                if __in_game_test(current_frame):

                    # read specified region of frame
                    region_ocr(current_frame, input_region, input_subregion)
                    # TODO connect & build region_ocr

            VOD.release()

    def __get_VOD_props(self, cap, des_time_interval=10):
        """[Returns width, height, fps, frame count, duration, desired time interval, frame index, and relative scale for any input video cap]

        Args:
            cap ([cv.VideoCapture(video)]): [cv mounted video capture]
            frame_number ([type]): [parse designated frame only, is None by default]
        """
        VOD_Props = {}

        VOD_Props["WIDTH"] = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        VOD_Props["HEIGHT"] = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        # where possible, stick to integers
        VOD_Props["FPS"] = int(cap.get(cv.CAP_PROP_FPS))
        VOD_Props["FRAME_COUNT"] = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
        VOD_Props["DURATION"] = (VOD_Props["FRAME_COUNT"] / VOD_Props["FPS"]) / 60
        VOD_Props["DESIRED_TIME_INTERVAL"] = des_time_interval * VOD_Props["FPS"]
        VOD_Props["FRAME_INDEX"] = range(
            0, VOD_Props["FRAME_COUNT"], VOD_Props["DESIRED_TIME_INTERVAL"]
        )
        VOD_Props["RELATIVE_SCALE"] = round((VOD_Props["HEIGHT"] * 100 / 2140), 0)

        return VOD_Props

    def ocr_status_update(self, current_frame_number, VOD_properties):

        # TODO make it print only at 5% intervals
        percent_complete = round(
            (current_frame_number * 100 / VOD_properties["FRAME_COUNT"]), 1
        )
        run_time = time_elapsed()

        print("{percent_complete}% complete; Elapsed time: {run_time}")

    def __in_game_test(self, input_frame):

        return None
