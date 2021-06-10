

def cache_img(input_img, out_name, view_img:=False, seconds:= 2):
    cv2.imwrite(f"lol_p4ocr/cache/{out_name}.png", input_img)
    cached_img = cv2.imread("lol_p4ocr/cache/{out_name}.png")

    if view_img is:
        cv2.imshow("Test View", input_img)
        cv2.waitKey(1000 * seconds)

    return cached_img

def draw_match_border(matches, input_img):
    
    for pt in zip(*matches[::-1]):
        cv2.rectangle(
            crop,
            pt,
            (pt[0] + scaled_w, pt[1] + scaled_h),
            (0, 255, 255),
            2,
        )

    # show what we found
    cv2.destroyAllWindows()
    cv2.imshow("Crop", crop)
    cv2.waitKey(1)

def resize_by_pxorpercent(input_img, desired_px=None, w_or_h=None, scale_percent=None):
    if w_or_h == "w":
        scale_percent = desired_px / input_img.shape[1] * 100
    elif w_or_h == "h":
        scale_percent = desired_px / input_img.shape[0] * 100

    width = int(input_img.shape[1] * scale_percent / 100)
    height = int(input_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(input_img, dim, interpolation=cv2.INTER_AREA)

    return resized

    
# Function: Mask frame's region of interest (RoI)

# Function: Resize frame's RoI

# Function: Blur frame's RoI

# Fucntion: Thresh frame's RoI