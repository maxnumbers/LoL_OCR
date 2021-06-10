
subregion_cfg = {
        "cs": {
            "image": cv2.imread("lol_p4ocr/templates/cs.png"),
            "threshold": 0.8,
            "config": "--psm 7 -c tessedit_char_whitelist=0123456789",
            "threshcfg": "",
        },
        "kda": {
            "image": cv2.imread("lol_p4ocr/templates/cs.png"),
            "threshold": 0.8,
            "config": "--psm 7 -c tessedit_char_whitelist=0123456789/",
            "threshcfg": "",
        },
        "gold": {
            "image": cv2.imread("lol_p4ocr/templates/gold.png"),
            "threshold": 0.8,
            "config": "--psm 7 -c tessedit_char_whitelist=0123456789",
            "threshcfg": "",
        },
        "time": {
            "image": "",
            "threshold": 0.8,
            "config": "--psm 7 -c tessedit_char_whitelist=0123456789:",
            "threshcfg": "",
        },
        "map": {
            "image": "",
            "threshold": 0.8,
            "config": "--psm 7 -c tessedit_char_whitelist=12345",
            "threshcfg": "",
        },
    }


masks = {
    "scoreboard": {
        "y1": 0,
        "y2": intpercent(height, 0.0303, 1),
        "x1": int(width - intpercent(height, 0.396, 1)),
        "x2": int(width),
        "scoreboard_subs": {
            "kda": {
                "y1": 0,
                "y2": 60,
                "x1": 400,
                "x2": 600,
            },
            "time": {
                "y1": 0,
                "y2": 60,
                "x1": 850,
                "x2": 1000,
            },
            "cs": {
                "y1": 0,
                "y2": 60,
                "x1": 670,
                "x2": 750,
            },
        },
    },
}