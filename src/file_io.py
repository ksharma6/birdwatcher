import matplotlib.pyplot as plt
import cv2

def txt_reader(path_to_txt):
    """Reads txt file and returns a list of lines with index removed

    Args:
        path_to_txt (str): path to txt file

    Returns:
        list: list of cleaned strings
    """
    f = open(path_to_txt)
    content = f.read()
    temp = content.splitlines()

    cleaned_content = []
    for s in temp:
        parts = s.split(' ', 1)
        if len(parts) > 1:
            new_string = parts[1]
        else:
            new_string = ''  # In case there is no space, return an empty string
        cleaned_content.append(new_string)

    return cleaned_content

def plot_images(file_paths, nrows, ncols):
    """plot image data into matplotlib plot

    Args:
        file_paths (list): list of image url's to plot
        nrows (int): number of rows for matplotlib plot
        ncols (int): number of cols for matplotlib plot
    """
    for i, file in enumerate(file_paths):
        img = cv2.imread(file, 1)
        plt.subplot(nrows,ncols,i+1)
        plt.title(img.shape, fontsize = 8)
        plt.axis('off')
        plt.imshow(img[:,:,::-1])
        plt.tight_layout()