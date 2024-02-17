import cv2
from tqdm import tqdm


def extract_frames(video_name: str) -> int:

    cap = cv2.VideoCapture(f"tempv/{video_name}")
    # video_fps = cap.get(cv2.CAP_PROP_FPS)

    success, frame = cap.read()
    # print(success, frame)
    frame_num = 0
    with tqdm(
        total=None,
        desc="Extracting frames",
    ) as pbar:
        while success:
            file_name = f"tempv/frames/{frame_num:015d}.jpg"
            cv2.imwrite(file_name, frame)
            success, frame = cap.read()
            frame_num += 1
            pbar.update(1)
    cap.release()
    return 0
